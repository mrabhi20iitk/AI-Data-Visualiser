

import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")



if not API_KEY:

    raise ValueError("OPENAI_API_KEY not found in .env")