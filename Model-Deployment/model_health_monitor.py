import time
import requests


class ModelHealthMonitor:
    def __init__(self, health_url, interval=30):
        self.health_url = health_url
        self.interval = interval

    def check_health(self):
        try:
            start = time.time()

            response = requests.get(
                self.health_url,
                timeout=5
            )

            latency = time.time() - start

            if response.status_code == 200:
                print(
                    f"Model API is healthy | "
                    f"Latency: {latency:.3f}s"
                )
            else:
                print(
                    f"Model API returned status: "
                    f"{response.status_code}"
                )

        except requests.RequestException as error:
            print(f"Health check failed: {error}")

    def run(self):
        print("Starting model health monitoring...")

        while True:
            self.check_health()
            time.sleep(self.interval)


if __name__ == "__main__":
    monitor = ModelHealthMonitor(
        health_url="http://localhost:8000/health",
        interval=30
    )

    monitor.run()
