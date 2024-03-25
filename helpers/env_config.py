import json


class EnvConfig:
    def __init__(self, account_id):
        self._account_id = account_id
        self._env_configs: dict = self._load_configs(self._account_id)

    @property
    def account_id(self):
        return self._account_id

    @property
    def env_configs(self) -> dict:
        return self._env_configs

    def _load_configs(self, account_id):
        with open("config.json") as config_file:
            configs = json.load(config_file)
            return configs[account_id]
