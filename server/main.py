from dotenv import load_dotenv
load_dotenv("../.env", override=True)

from fastapi import FastAPI
import os
from src.events import startup, shutdown
from contextlib import asynccontextmanager
from src.routes import main_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup(app)
    try:
        yield
    finally:
        await shutdown(app)

app = FastAPI(lifespan=lifespan)

app.include_router(main_router)

from src.middlewares import middlewares_to_apply

# Add middlewares in reverse order they were discovered
# FastAPI executes the LAST added middleware FIRST for incoming requests.
for middleware in reversed(middlewares_to_apply):
    app.add_middleware(middleware)


if __name__ == "__main__":
    import uvicorn

    DEFAULT_PORT = "8000"
    try:
        port = int(os.environ.get("PORT", DEFAULT_PORT))
    except Exception:
        port = int(DEFAULT_PORT)

    uvicorn.run(
        "main:app",
        port=port,
        host=os.environ.get("HOST", "0.0.0.0"),
        reload=os.environ.get("ENV", "DEV") == "DEV",
    )
