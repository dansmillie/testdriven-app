# services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Dev config"""
    pass

class TestingConfig(BaseConfig):
    """Testing config"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production config"""
    pass
