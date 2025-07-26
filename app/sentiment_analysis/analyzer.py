# app/sentiment_analysis/analyzer.py
import logging
from transformers import pipeline
from app.common.config import Config
from typing import Dict

logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    _instance = None

    def __init__(self):
        try:
            self.pipeline = pipeline(
                "sentiment-analysis",
                model=Config.SENTIMENT_MODEL,
                device_map="auto",
                truncation=True
            )
            logger.info(f"Loaded sentiment model: {Config.SENTIMENT_MODEL}")
        except Exception as e:
            logger.error(f"Model loading failed: {e}")
            raise

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def analyze(self, text: str) -> Dict[str, any]:
        try:
            result = self.pipeline(text[:Config.MAX_TEXT_LENGTH])[0]
            return {
                "sentiment": result["label"].upper(),
                "score": float(result["score"])
            }
        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            return {"sentiment": "NEUTRAL", "score": 0.5}
