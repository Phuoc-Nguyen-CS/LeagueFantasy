import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import pandas as pd


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "World World"}

@app.get("/players")
def get_players():
    df = pd.read_csv("output.csv")
    df = df.astype(str)
    return jsonable_encoder(df.to_dict(orient="records"))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
