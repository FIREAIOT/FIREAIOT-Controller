import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def env(key):
	return os.getenv(key)