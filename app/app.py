from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def func1():
    return {"Hello": "/"}

@app.get("/ping")
def func2():
    return {"Hello": "/ping"}

@app.get("/ping/ping")
def func3():
    return {"Hello": "/ping/ping"}

handler = Mangum(app)