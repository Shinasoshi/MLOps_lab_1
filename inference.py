from pathlib import Path

import joblib


CLASS_NAMES = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


class IrisModelService:
    def __init__(self, model_path: str = "iris_model.joblib"):
        self.model_path = Path(model_path)
        self.model = self.load_model()

    def load_model(self):
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        return joblib.load(self.model_path)

    def predict(self, features: dict) -> str:
        values = [
            [
                features["sepal_length"],
                features["sepal_width"],
                features["petal_length"],
                features["petal_width"],
            ]
        ]
        prediction_idx = self.model.predict(values)[0]
        return CLASS_NAMES[int(prediction_idx)]
