"""
Configuration file for Flask application
Different configurations for development and production
"""

import os

class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max request size
    
    # Model settings
    MODEL_CACHE_ENABLED = True
    MODEL_TIMEOUT = 30  # seconds
    
    # CORS settings (if needed for frontend)
    CORS_ENABLED = True
    CORS_ORIGINS = "*"

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration for PythonAnywhere"""
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    
    # Performance settings
    JSON_SORT_KEYS = False
    SEND_FILE_MAX_AGE_DEFAULT = 604800  # 1 week

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True

# Load configuration based on environment
def get_config():
    """Get appropriate config based on environment"""
    env = os.environ.get('FLASK_ENV', 'production')
    
    if env == 'development':
        return DevelopmentConfig()
    elif env == 'testing':
        return TestingConfig()
    else:
        return ProductionConfig()
