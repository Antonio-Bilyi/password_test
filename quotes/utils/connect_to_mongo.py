from mongoengine import connect

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env_path = BASE_DIR / '.env'

load_dotenv(dotenv_path=env_path)

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASS')
domain = os.getenv('MONGO_DOMAIN')
db_name = os.getenv('MONGO_DBNAME')

def connect_to_db():

    connect(
        host=f"""mongodb+srv://{user}:{password}@{domain}/{db_name}?retryWrites=true&w=majority""",
        tls=True
    )

if __name__ == '__main__':

    connect_to_db()