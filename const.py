from os import getenv

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    pass

ZPA_BASE_URL: str = getenv('ZPA_SCIM_BASE_URL', '')
ZPA_TOKEN: str = getenv('ZPA_SCIM_TOKEN', '')

ZIA_BASE_URL: str = getenv('ZIA_SCIM_BASE_URL', '')
ZIA_TOKEN: str = getenv('ZIA_SCIM_TOKEN', '')