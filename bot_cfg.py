from tg_datastore import TGDataStore
from json import dumps


def write_config():
    global global_config
    datastore.write_field(datastore_field_id, global_config)


def read_config() -> dict:
    global global_config
    global_config = datastore.read_field(datastore_field_id)


tg_api_id = 16643256
tg_api_hash = "000d66c8f9c490c81dd64d7a48f55d1d"
tg_bot_token = "5637489619:AAEUpmDTNu0CjcCe5mwoDoO9A9E0mq3RCmI"
datastore_store_id 5269238222
datastore_field_id = 2
global_config = {}

datastore = TGDataStore(tg_bot_token, datastore_store_id)

read_config()
print("Config:\n", dumps(global_config, indent=4))
