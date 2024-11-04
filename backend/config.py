import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self):
        self.DB_URL = self.fetch_env_var("DB_URL", "sqlite:///default.db")
        self.API_KEY = self.fetch_env_var("API_KEY", "default_api_key")
        self.SERVER_PORT = self.fetch_env_var("SERVER_PORT", "8000", cast=int)

    def fetch_env_var(self, var_name, default=None, cast=str):
        value = os.getenv(var_name, default)
        if value is None:
            raise ConfigError(f"Missing essential environment variable: {var_name}")
        try:
            return cast(value)
        except ValueError:
            raise ConfigError(f"Invalid format for environment variable: {var_name}")

try:
    config = Config()
except ConfigError as e:
    print(f"Error in configuration: {e}")

if __name__ == "__main__":
    print(config.DB_URL)
    print(config.API_KEY)
    print(config.SERVER_PORT)