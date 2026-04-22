from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from inference import IrisModelService

app = FastAPI()
model = IrisModelService()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = model.predict(request.model_dump())
    return PredictResponse(prediction=prediction)
