import os

from dotenv import load_dotenv


load_dotenv()


DB_URL = os.getenv("DB_URL")

if not DB_URL:
    raise RuntimeError("DB_URL não definida")
