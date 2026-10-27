from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http = httpx.AsyncClient(timeout=60.0)
    yield
    await app.state.http.aclose()



app = FastAPI(title="Auction House Tracker", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok", "realm": settings.connected_realm_id}
