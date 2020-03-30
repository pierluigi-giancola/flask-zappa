
class DefaultFlaskConfig(object):
    DEBUG = False
    TESTING = False
    JWT_ALGORITHM = 'HS512'
    JWT_SECRET_KEY = 'Asjfwol2asf123142Ags1k23hnSA36as6f4qQ324FEsvb'

class DefaultCustomConfig(DefaultFlaskConfig):
    PROJECT_NAME='blink-delivery'

class dev(DefaultCustomConfig):
    DEBUG=True
    TESTING=True
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://dbaccess:qQD2xSZfb25ujWU6@blink-staging-lf76o.mongodb.net/test?retryWrites=true&w=majority'
    }

class staging(DefaultCustomConfig):
    DEBUG=True
    TESTING=True
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://dbaccess:qQD2xSZfb25ujWU6@blink-staging-lf76o.mongodb.net/test?retryWrites=true&w=majority'
    }

class prod(DefaultCustomConfig):
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://dbaccess:oMopBbcd5dyUi6Nw@blink-prod-je4nb.mongodb.net/delivery?retryWrites=true&w=majority'
    }