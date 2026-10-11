from fastapi import FastAPI
import os
from src.utils import logger

async def shutdown(app: FastAPI):
    logger.info(f"Stopping Application")

