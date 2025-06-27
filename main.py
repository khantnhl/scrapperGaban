import os
from dotenv import load_env
import requests
from bs4 import BeautifulSoup
import pandas as pd

load_env()

TWITTER_APIKEY = os.environ["APIKEY"]
