import math
def transform_time_to_cyclic(hour):
    sin_val = math.sin(2 * math.pi * hour / 24)
    cos_val = math.cos(2 * math.pi * hour / 24)
    return sin_val, cos_val

def calculate_time_difference(hour1, hour2):
    sin1, cos1 = transform_time_to_cyclic(hour1)
    sin2, cos2 = transform_time_to_cyclic(hour2)
    return math.sqrt((sin2 - sin1) ** 2 + (cos2 - cos1) ** 2)
