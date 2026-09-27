from fastapi import FastAPI
from fastapi_cli import cli

# Инцилизация FastAPI приложения #
app = FastAPI()


# пишем тестовую ручку Hello World #
@app.get("/")
def test():
    return {"message": "Hello World"}