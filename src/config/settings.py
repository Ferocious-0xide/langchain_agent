from pathlib import Path
import os
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
env_path = Path(__file__).parents[2] / '.env'
logger.info(f"Looking for .env file at: {env_path}")
load_dotenv(dotenv_path=env_path)

class Settings:
    """Configuration settings loaded from environment variables."""
    
    def __init__(self):
        logger.info("Initializing settings...")
        # API Keys
        self.ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
        self.NEWS_API_KEY = os.getenv('NEWS_API_KEY')
        
        # Log status of each key (safely)
        if self.ANTHROPIC_API_KEY:
            logger.info("ANTHROPIC_API_KEY loaded successfully")
        else:
            logger.warning("ANTHROPIC_API_KEY not found")
            
        if self.NEWS_API_KEY:
            logger.info("NEWS_API_KEY loaded successfully")
        else:
            logger.warning("NEWS_API_KEY not found")
    
    def validate(self) -> tuple[bool, list[str]]:
        """Validate the configuration settings."""
        errors = []
        
        if not self.ANTHROPIC_API_KEY:
            errors.append("ANTHROPIC_API_KEY is required")
        if not self.NEWS_API_KEY:
            errors.append("NEWS_API_KEY is required")
            
        return (len(errors) == 0, errors)

# Create a global settings instance
settings = Settings()

if __name__ == "__main__":
    # Test the settings
    is_valid, errors = settings.validate()
    if is_valid:
        print("Settings validated successfully!")
    else:
        print("Settings validation failed:", errors)