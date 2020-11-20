class DefaultFlaskConfig(object):
    DEBUG = False
    TESTING = False


class DefaultCustomConfig(DefaultFlaskConfig):
    PROJECT_NAME = 'blink-webhook-interface'


class dev(DefaultCustomConfig):
    DEBUG = True
    TESTING = True


class prod(DefaultCustomConfig):
    pass
