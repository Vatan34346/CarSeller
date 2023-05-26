import os
from dotenv import load_dotenv

load_dotenv()


class EnvHandler:
    @staticmethod
    def get_env_var(name):
        return os.getenv(name)

