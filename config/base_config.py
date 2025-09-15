# config/base_config.py
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration management with environment variables"""
    
    def __init__(self, environment=None):
        self.environment = environment or os.getenv('ENVIRONMENT', 'qa')
        self.load_environment_config()
    
    def load_environment_config(self):
        """Load environment-specific configuration"""
        config_path = Path(__file__).parent / "environments" / f"{self.environment}.json"

        if config_path.exists():
            with open(config_path, 'r') as f:
                config_data = json.load(f)
            self.__dict__.update(config_data)
            
    
    def get_username(self):
        # Get environment-specific username
        return os.getenv(f'SF_{self.environment.upper()}_USERNAME') or os.getenv('SF_USERNAME')
    
    def get_password(self):
        # Get environment-specific password  
        return os.getenv(f'SF_{self.environment.upper()}_PASSWORD') or os.getenv('SF_PASSWORD')
        
    
    def get_base_url(self):
        return getattr(self, 'base_url', 'https://login.salesforce.com')

# Singleton instance
config = Config()