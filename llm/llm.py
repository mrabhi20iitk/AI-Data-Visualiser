import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

from llm.config import API_KEY


llm  = ChatGroq(model="openai/gpt-oss-120b",api_key=API_KEY)