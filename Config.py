import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
else:
    # Fill the Values
    API_ID = 17338150
    API_HASH = "a855f783b521cbecef19e0e5dca232de"
    BOT_TOKEN = "5550501271:AAH97Hlh1U9G_ZHLm9hD6KjvrSA_RJ6GW3o"
    DATABASE_URL = "mongodb+srv://Dyler:aa112233@cluster0.dz7osmg.mongodb.net/?retryWrites=true&w=majority"
