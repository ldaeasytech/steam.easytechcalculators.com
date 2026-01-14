from fastapi import FastAPI
from thermo import water_props

app = FastAPI(title="Steam Property API")

@app.get("/api/water")
def calculate(T: float, P: float):
    """
    T: °C
    P: MPa
    """
    return water_props(T, P)
