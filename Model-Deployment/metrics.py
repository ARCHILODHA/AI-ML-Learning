import time
from collections import defaultdict


class ModelMetrics:

    def __init__(self):
        self.total_requests = 0
        self.total_errors = 0
        self.total_latency = 0
        self.predictions = defaultdict(int)

    def record_request(self):
        self.total_requests += 1

    def record_error(self):
        self.total_errors += 1

    def record_latency(self, latency):
        self.total_latency += latency

    def record_prediction(self, prediction):
        self.predictions[str(prediction)] += 1

    def get_summary(self):

        average_latency = (
            self.total_latency / self.total_requests
            if self.total_requests > 0
            else 0
        )

        error_rate = (
            self.total_errors / self.total_requests
            if self.total_requests > 0
            else 0
        )

        return {
            "total_requests": self.total_requests,
            "total_errors": self.total_errors,
            "average_latency": average_latency,
            "error_rate": error_rate,
            "predictions": dict(self.predictions)
        }


metrics = ModelMetrics()
