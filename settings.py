class Configuration(object):

    def __init__(self):

        config = {
            'mysql': {
                'driver': 'mysql',
                'host': 'localhost',
                'database': '',
                'user': 'username',
                'password': 'password',
                'prefix': ''
            }
        }
        self.config = config
