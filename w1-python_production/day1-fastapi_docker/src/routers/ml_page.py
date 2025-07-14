import os
import pickle

from fastapi.routing import APIRouter
from src.models.IRIS import IrisModel


CLASSES = ['setosa', 'versicolor', 'virginica']
MODEL_PATH = "train_ml/iris_model.pkl"

def load_model():
    """
    Load the trained model from the specified path.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    
    return model

model = load_model()

iris_example = IrisModel(
    sepal_length=10,
    sepal_width=5,
    petal_length=3,
    petal_width=4,
)

ml_router = APIRouter()
@ml_router.get("/predict")
@ml_router.post("/predict")
async def predict(iris: IrisModel = iris_example):
    """
    Predict the iris species based on the provided features.
    """
    features = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    prediction = model.predict(features)
    return {"message": "Prediction successful", "data_sample": iris, "prediction": CLASSES[int(prediction[0])]}