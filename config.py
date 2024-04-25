import os

API_ID = API_ID = 20352686

API_HASH = os.environ.get("API_HASH", "d0c3424472358f66d8dbddfdb7017730")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6956263556:AAESxqNLatcl7oZ4IEBStspCZvo8HjRK6P8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER",6982484823))

LOG = -   -1002113257984         #don't change it otherwise you face error while deploying.
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "Your user id").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
