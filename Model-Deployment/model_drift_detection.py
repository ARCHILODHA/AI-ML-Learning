
import numpy as np
from scipy.stats import ks_2samp


class ModelDriftDetector:
    def __init__(self, threshold=0.05):
        self.threshold = threshold

    def detect_drift(self, reference_data, current_data):
        reference_data = np.asarray(reference_data)
        current_data = np.asarray(current_data)

        if reference_data.ndim != 2 or current_data.ndim != 2:
            raise ValueError("Both datasets must be two-dimensional.")

        if reference_data.shape[1] != current_data.shape[1]:
            raise ValueError("Datasets must have equal feature counts.")

        results = []

        for feature_index in range(reference_data.shape[1]):
            statistic, p_value = ks_2samp(
                reference_data[:, feature_index],
                current_data[:, feature_index]
            )

            results.append({
                "feature": feature_index,
                "statistic": float(statistic),
                "p_value": float(p_value),
                "drift_detected": p_value < self.threshold
            })

        return results


if __name__ == "__main__":
    np.random.seed(42)

    reference = np.random.normal(50, 10, (1000, 3))
    current = np.random.normal(60, 10, (1000, 3))

    detector = ModelDriftDetector()
    report = detector.detect_drift(reference, current)

    for result in report:
        print(result)
