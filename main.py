from fastapi import FastAPI
from pydantic import BaseModel
import onnxruntime as rt
import pandas as pd
import numpy as np

app = FastAPI()

try:
    sess = rt.InferenceSession("best_model.onnx")
except Exception as e:
    print(f"Błąd podczas ładowania modelu ONNX: {e}")
    sess = None

class PredictionInput(BaseModel):
    unemp: float
    wage: float
    distance: float
    tuition: float
    education: float

# Endpoint do przewidywania wyniku
@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        if sess is None:
            return {"error": "Model nie został załadowany. Sprawdź, czy plik modelu istnieje i jest poprawny."}

        data = pd.DataFrame([input_data.dict()])

        data = pd.get_dummies(data)
        required_columns = [f"column_{i}" for i in range(14)]
        for col in required_columns:
            if col not in data.columns:
                data[col] = 0
        data = data[required_columns]

        input_array = data.to_numpy().astype(np.float32)

        input_name = sess.get_inputs()[0].name
        pred_onx = sess.run(None, {input_name: input_array})

        predicted_score = float(pred_onx[0][0])
        return {"predicted_score": predicted_score}

    except Exception as e:
        print(f"Błąd: {e}")
        return {"error": f"Wystąpił błąd podczas przetwarzania żądania: {e}"}