
from pydantic import BaseModel, Field, ValidationError
from typing import List


class PredictionInput(BaseModel):
    age: int = Field(gt=0, lt=120)
    monthly_charges: float = Field(ge=0)
    tenure: int = Field(ge=0, le=100)

    def to_model_input(self):
        return [[
            self.age,
            self.monthly_charges,
            self.tenure
        ]]


def validate_prediction_input(payload):
    try:
        validated_data = PredictionInput(**payload)

        return {
            "valid": True,
            "model_input": validated_data.to_model_input()
        }

    except ValidationError as error:
        return {
            "valid": False,
            "errors": error.errors()
        }


if __name__ == "__main__":
    sample = {
        "age": 25,
        "monthly_charges": 499.50,
        "tenure": 12
    }

    result = validate_prediction_input(sample)

    print(result)
