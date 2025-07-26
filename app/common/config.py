import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Config:
    # Docker Configuration
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    
    # Path Configuration
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = BASE_DIR / "app" / "data"
    MODELS_DIR = BASE_DIR / "models"
    
    # Database Paths
    SQLITE_PATH = DATA_DIR / "sentiments.db"
    CHROMA_PATH = DATA_DIR / "chroma_db"
    
    # Model Names
    SENTIMENT_MODEL = os.getenv("SENTIMENT_MODEL", "cardiffnlp/twitter-roberta-base-sentiment-latest")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    
    # API Limits
    MAX_TEXT_LENGTH = 2000
    MAX_CONTEXTS = 5
    MAX_BATCH_SIZE = 20

    @classmethod
    def initialize(cls):
        """Ensure directories exist and configure environment"""
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.MODELS_DIR.mkdir(parents=True, exist_ok=True)
        os.environ["ANONYMIZED_TELEMETRY"] = "False"
        logger.info(f"Configuration initialized - Models: {cls.SENTIMENT_MODEL}")

# Initialize on import
Config.initialize()