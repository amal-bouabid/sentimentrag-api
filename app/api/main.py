# app/api/main.py
import logging
import uuid
import sqlite3
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.sentiment_analysis.analyzer import SentimentAnalyzer
from app.rag.rag_pipeline import RAGPipeline
from app.api.models import TextInput, AnalysisResponse
from app.common.config import Config
from typing import List

logger = logging.getLogger(__name__)

app = FastAPI(
    title="SentimentRAG API",
    description="Analyse de sentiment enrichie par RAG",
    version="1.0.0",
    docs_url="/docs" if Config.DEBUG else None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    conn = sqlite3.connect(Config.SQLITE_PATH, check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sentiments (
            id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            score REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    try:
        yield conn
    finally:
        conn.close()

@app.on_event("startup")
async def startup_event():
    logger.info(f"API started on {Config.API_HOST}:{Config.API_PORT}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "models": {
            "sentiment": Config.SENTIMENT_MODEL,
            "embedding": Config.EMBEDDING_MODEL
        }
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze(
    request: TextInput,
    analyzer: SentimentAnalyzer = Depends(SentimentAnalyzer.get_instance),
    rag: RAGPipeline = Depends(RAGPipeline.get_instance),
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        result = analyzer.analyze(request.text)
        text_id = str(uuid.uuid4())
        db.execute(
            "INSERT INTO sentiments VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)",
            (text_id, request.text, result["sentiment"], result["score"])
        )
        db.commit()

        rag_response = await rag.process(request.text, request.context_texts, text_id)

        return AnalysisResponse(
            sentiment=result["sentiment"],
            score=result["score"],
            rag_response=rag_response
        )
    except Exception as e:
        logger.exception("Analysis failed")
        raise HTTPException(500, "Internal server error")