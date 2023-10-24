from fastapi import FastAPI
import uvicorn
from config import settings
from src.auth.utils import PROTECTED
from src.user.router import router as router_user
from src.auth.router import router as router_auth

app = FastAPI(
    title="FastAPI Demo App",
    description=("Demonstration of FastAPI"),
    version="0.0.1",
    docs_url="/api",
    redoc_url="/api/doc",
)

app.include_router(router_user, dependencies=PROTECTED)
app.include_router(router_auth)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
