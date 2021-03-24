import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1638391726:AAHzcRm1omosXrr9CZog0dUraAVEl2TKAU4"
    APP_ID = "1248019"
    API_HASH = "dc8f87c2d1126bb2ac4ed258a4941e05"
