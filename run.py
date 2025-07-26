import uvicorn
from app.common.config import get_config

if __name__ == "__main__":
    config = get_config()
    uvicorn.run(
        "app.api.main:app",
        host=config.get("api.host", "0.0.0.0"),
        port=config.get("api.port", 8000),
        reload=config.get("api.debug", False)
    )