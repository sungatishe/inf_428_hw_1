import unittest
import numpy as np

from task_2.calculate.calculate import generate_random_data, calculate_aggregated_threat_score


class TestThreatScoreFunctions(unittest.TestCase):

    def test_generate_random_data_within_range(self):
        mean, variance, num_samples = 30, 10, 100
        data = generate_random_data(mean, variance, num_samples)
        self.assertTrue(np.all(data >= max(0, mean - variance)))
        self.assertTrue(np.all(data <= min(90, mean + variance)))
        self.assertEqual(len(data), num_samples)

    def test_generate_random_data_upper_limit(self):
        mean, variance, num_samples = 85, 10, 50
        data = generate_random_data(mean, variance, num_samples)
        self.assertTrue(np.all(data <= 90))

    def test_calculate_aggregated_threat_score_basic(self):
        department_scores = [
            [10, 20, 30],
            [20, 30, 40],
            [30, 40, 50]
        ]
        importance_tags = [1, 1, 1]  # Одинаковая важность
        expected_score = np.mean([10, 20, 30, 20, 30, 40, 30, 40, 50])  # Среднее значение
        aggregated_score = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertAlmostEqual(aggregated_score, expected_score)

    def test_calculate_aggregated_threat_score_with_importance(self):
        department_scores = [
            [10, 20, 30],
            [20, 30, 40],
            [30, 40, 50]
        ]
        importance_tags = [1, 2, 3]  # Разная важность
        weighted_mean = (np.mean([10, 20, 30]) * 1 +
                         np.mean([20, 30, 40]) * 2 +
                         np.mean([30, 40, 50]) * 3) / sum(importance_tags)
        aggregated_score = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertAlmostEqual(aggregated_score, weighted_mean)

    def test_calculate_aggregated_threat_score_all_zero(self):
        department_scores = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        importance_tags = [1, 1, 1]
        aggregated_score = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertEqual(aggregated_score, 0)

    def test_calculate_aggregated_threat_score_max_threat(self):
        department_scores = [
            [90, 90, 90],
            [90, 90, 90],
            [90, 90, 90]
        ]
        importance_tags = [1, 1, 1]
        aggregated_score = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertEqual(aggregated_score, 90)

    def test_calculate_aggregated_threat_score_with_high_variance(self):
        department_scores = [
            generate_random_data(mean=30, variance=20, num_samples=100),
            generate_random_data(mean=50, variance=30, num_samples=120),
            generate_random_data(mean=20, variance=15, num_samples=80)
        ]
        importance_tags = [2, 3, 1]
        aggregated_score = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertTrue(0 <= aggregated_score <= 90)


if __name__ == '__main__':
    unittest.main()
