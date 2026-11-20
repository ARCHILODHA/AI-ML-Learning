import joblib
import pandas as pd


class BatchPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict_file(self, input_file, output_file):
        data = pd.read_csv(input_file)

        predictions = self.model.predict(data)

        data["prediction"] = predictions

        data.to_csv(output_file, index=False)

        print(f"Predictions saved to {output_file}")

        return data


if __name__ == "__main__":
    predictor = BatchPredictor("model.joblib")

    result = predictor.predict_file(
        input_file="input.csv",
        output_file="predictions.csv"
    )

    print(result.head())
