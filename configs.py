# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = 2992000
    API_HASH = "235b12e862d71234ea222082052822fd"
    BOT_TOKEN = "5832484897:AAF6qiaK61WF1vJWZxUTDov1g0z4YJ-UhGk"
    DOWNLOAD_DIR = "./downloads"
    LOGGER = logging
    OWNER_ID = 5351121397
    PRO_USERS = []
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = "mongodb+srv://Vasusen:darkmaahi@cluster0.o7uqb.mongodb.net/cluster0?retryWrites=true&w=majority"
    LOG_CHANNEL = int("-1001879806908")
    BROADCAST_AS_COPY = False
    
    
