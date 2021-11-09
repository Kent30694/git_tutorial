import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

url = os.environ.get('URL')
key = os.environ.get("KEY")
host = os.environ.get("HOST")

print(url)

