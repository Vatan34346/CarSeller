from src.helpers.envhelper import EnvHandler


class AuthHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if EnvHandler.get_env_var('LEVAN_USERNAME') == self.username and EnvHandler.get_env_var('LEVAN_PAROL') == self.password:
            return 'User exists'
        else:
            return 'No such user'
