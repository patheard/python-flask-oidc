import os
from dotenv import load_dotenv

load_dotenv()

IDP_ACR_VALUES = os.getenv("IDP_ACR_VALUES")
IDP_CONF_URL = os.getenv("IDP_CONF_URL")

LOGINGOV_CLIENT_ID = os.getenv("LOGINGOV_CLIENT_ID")
LOGINGOV_CLIENT_PRIVATE_KEY = os.getenv("LOGINGOV_CLIENT_PRIVATE_KEY")
with open(LOGINGOV_CLIENT_PRIVATE_KEY, "rb") as f:
    LOGINGOV_CLIENT_SECRET = f.read()
