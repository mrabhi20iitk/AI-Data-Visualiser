from dotenv import load_dotenv
from sqlalchemy import create_engine
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")



def get_engine():

    engine = create_engine(DATABASE_URL)

    return engine