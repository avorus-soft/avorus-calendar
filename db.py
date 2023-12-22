import os
from urllib.parse import quote_plus

import motor.motor_asyncio

mongodb_url = 'mongodb://%s:%s@%s:27017/%s' % tuple(map(
    quote_plus, (os.environ['MONGO_INITDB_USERNAME'], os.environ['MONGO_INITDB_PASSWORD'], os.environ['MONGO_INITDB_HOSTNAME'], os.environ['MONGO_INITDB_DATABASE'])))

client = motor.motor_asyncio.AsyncIOMotorClient(
    mongodb_url, uuidRepresentation='standard'
)
db = client['calendar']
