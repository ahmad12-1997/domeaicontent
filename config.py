
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    DEBUG = True
    
class ProductionConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    DEBUG= False

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': ProductionConfig,
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
