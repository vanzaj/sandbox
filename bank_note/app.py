from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
import joblib


class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

ml = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    ml["model"] = joblib.load("./ml/bank_note_model.joblib")
    yield
    ml.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def get_name(name: str):
    return {"message": f"Hello {name}"}


@app.get("/model/info")
async def get_model_info():
    print(ml)
    name = type(ml["model"]).__name__
    data = {"model": {"name": name, "accuracy": model.accuracy}}
    return data


@app.post("/model/predict")
async def predict_banknote(banknote: BankNote):
    data = [[banknote.variance, banknote.skewness, banknote.curtosis, banknote.entropy]]
    prediction = ml["model"].predict(data)
    if prediction[0] == 1:
        prediction = "Fake Bank note"
    else:
        prediction = "Real Bank note"
    return {"prediction": prediction}
