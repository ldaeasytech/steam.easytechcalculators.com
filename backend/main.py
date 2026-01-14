from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from thermo import water_props

app = FastAPI()

# ⚠️ Add CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://steam.easytechcalculators.com"],  # your frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, etc.
    allow_headers=["*"],  # allows all headers
)

@app.get("/api/water")
def calculate(T: float, P: float):
    return water_props(T, P)
