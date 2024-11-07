import numpy as np


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(department_scores, importance_tags):
    weighted_scores = [
        np.mean(scores) * importance for scores, importance in zip(department_scores, importance_tags)
    ]
    total_importance = sum(importance_tags)
    aggregated_score = sum(weighted_scores) / total_importance
    return min(max(aggregated_score, 0), 90)  # Ограничиваем в пределах 0–90


# Пример использования:
department_scores = [
    generate_random_data(mean=30, variance=10, num_samples=100),  # Engineering
    generate_random_data(mean=40, variance=15, num_samples=120),  # Marketing
    generate_random_data(mean=25, variance=20, num_samples=80),  # Finance
    generate_random_data(mean=35, variance=10, num_samples=150),  # HR
    generate_random_data(mean=45, variance=5, num_samples=60)  # Science
]
importance_tags = [3, 4, 2, 5, 3]  # Важность каждого департамента

aggregated_score = calculate_aggregated_threat_score(department_scores, importance_tags)
print("Aggregated User Threat Score:", aggregated_score)
