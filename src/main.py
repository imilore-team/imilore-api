from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.init import engine, DeclarativeBase

from src.routes.feedback import router as feedback_router
from src.routes.ml_data import router as ml_data_router


DeclarativeBase.metadata.create_all(bind=engine)
DeclarativeBase.metadata.bind = engine


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(feedback_router)
app.include_router(ml_data_router)
