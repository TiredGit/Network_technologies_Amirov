from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def welcome():
    return "Hello! My name is Amirov Eduard!"
