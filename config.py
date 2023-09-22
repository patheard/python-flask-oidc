import os
from dotenv import load_dotenv

load_dotenv()

IDENTITY_PROVIDER_CONF_URL = os.getenv("IDENTITY_PROVIDER_CONF_URL")

LOGINGOV_CLIENT_ID = os.getenv("LOGINGOV_CLIENT_ID")
LOGINGOV_CLIENT_PRIVATE_KEY = os.getenv("LOGINGOV_CLIENT_PRIVATE_KEY")
with open(LOGINGOV_CLIENT_PRIVATE_KEY, "rb") as f:
    LOGINGOV_CLIENT_SECRET = f.read()
