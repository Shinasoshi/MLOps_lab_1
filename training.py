from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    return load_iris()


def train_model():
    data = load_data()
    model = RandomForestClassifier(random_state=42)
    model.fit(data.data, data.target)
    return model


def save_model(model, path: str = "iris_model.joblib") -> None:
    output_path = Path(path)
    joblib.dump(model, output_path)


if __name__ == "__main__":
    trained_model = train_model()
    save_model(trained_model)
    print("Model saved to iris_model.joblib")
