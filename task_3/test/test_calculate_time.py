import math
import unittest

from task_3.time_calculate.calculate_time import transform_time_to_cyclic, calculate_time_difference


class TestCyclicTimeTransformation(unittest.TestCase):

    def test_transform_time_to_cyclic(self):
        # Test basic transformations with separate element checks
        sin_0, cos_0 = transform_time_to_cyclic(0)
        self.assertAlmostEqual(sin_0, 0, places=5)
        self.assertAlmostEqual(cos_0, 1, places=5)

        sin_6, cos_6 = transform_time_to_cyclic(6)
        self.assertAlmostEqual(sin_6, 1, places=5)
        self.assertAlmostEqual(cos_6, 0, places=5)

        sin_12, cos_12 = transform_time_to_cyclic(12)
        self.assertAlmostEqual(sin_12, 0, places=5)
        self.assertAlmostEqual(cos_12, -1, places=5)

        sin_18, cos_18 = transform_time_to_cyclic(18)
        self.assertAlmostEqual(sin_18, -1, places=5)
        self.assertAlmostEqual(cos_18, 0, places=5)

    def test_calculate_time_difference_direct(self):
        # Test for direct difference calculation without crossing midnight
        distance = calculate_time_difference(3, 5)
        # Expected value recalculated to align with Euclidean distance on the unit circle
        expected_distance = math.sqrt((transform_time_to_cyclic(3)[0] - transform_time_to_cyclic(5)[0]) ** 2 +
                                      (transform_time_to_cyclic(3)[1] - transform_time_to_cyclic(5)[1]) ** 2)
        self.assertAlmostEqual(distance, expected_distance, places=5)

    def test_calculate_time_difference_across_midnight(self):
        # Test crossing midnight (23:00 to 01:00)
        distance = calculate_time_difference(23, 1)
        expected_distance = math.sqrt((transform_time_to_cyclic(23)[0] - transform_time_to_cyclic(1)[0]) ** 2 +
                                      (transform_time_to_cyclic(23)[1] - transform_time_to_cyclic(1)[1]) ** 2)
        self.assertAlmostEqual(distance, expected_distance, places=5)

    def test_calculate_time_difference_same_hour(self):
        # Difference between the same hour should be zero
        self.assertAlmostEqual(calculate_time_difference(8, 8), 0, places=5)

    def test_calculate_time_difference_max_distance(self):
        # Maximum difference between opposite times (e.g., 0 and 12)
        self.assertAlmostEqual(calculate_time_difference(0, 12), 2, places=5)

if __name__ == '__main__':
    unittest.main()