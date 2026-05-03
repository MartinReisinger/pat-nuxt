import os
from dotenv import load_dotenv      # to read the api key form a .env file
from google import genai            # to use google generative ai via api key in python

# loading the hidden environment variable from .env (google api key)
load_dotenv()

client = genai.Client()
model_id = 'gemin-3.0-flash'

