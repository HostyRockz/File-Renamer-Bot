import logging
from pyrogram import Client
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from sample_config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)

app = Client(
     'PythonBot',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins = plugins
)

app.run()
