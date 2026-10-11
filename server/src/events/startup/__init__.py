from fastapi import FastAPI
import os
from src.utils import logger

async def startup(app: FastAPI):
    logger.info(f"Starting Application")
