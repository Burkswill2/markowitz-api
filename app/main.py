from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import markowitz_model

app = FastAPI(
    title="markowitz-api",
    description="Markowitz mean-variance portfolio optimizer",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(markowitz_model.router)


@app.get("/")
async def root():
    return {"service": "markowitz-api", "docs": "/docs"}
