import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 19121146))

    API_HASH = os.environ.get("API_HASH", "92449d5960afebc20ff2ae1d2f22844f")
