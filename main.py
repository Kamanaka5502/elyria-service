from fastapi import FastAPI
from routers import gate, rate, session

app = FastAPI(
    title="Elyria Service",
    version="0.4.0"
)

@app.get("/")
def root():
    return {"status": "alive"}

app.include_router(gate.router)
app.include_router(rate.router)
app.include_router(session.router)
