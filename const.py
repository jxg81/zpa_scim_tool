from os import getenv

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    pass

BASE_URL: str = getenv('ZPA_SCIM_BASE_URL', '')
TOKEN: str = getenv('ZPA_SCIM_TOKEN', '')