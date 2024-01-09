import pathlib

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

ROOT = pathlib.Path(__file__).resolve().parent  # twitter-airflow-project/
BASE_DIR = ROOT.parent  # twitter-airflow-project
config = Config(BASE_DIR / ".env")

# Twitter configs.
ACCESS_KEY = config("ACCESS_KEY", str)
ACCESS_SECRET = config("ACCESS_SECRET", str)
CONSUMER_KEY = config("CONSUMER_KEY", str)
CONSUMER_SECRET = config("CONSUMER_SECRET", str)
BEARER_TOKEN = config("BEARER_TOKEN", str)


