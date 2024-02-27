import json
import logging
import os

from dotenv import load_dotenv

class Config:

    @property
    def mongo_host(self) -> str:
        return self.__mongo_host

    @property
    def mongo_port(self) -> int:
        return self.__mongo_port

    @property
    def database_name(self) -> str:
        return self.__database_name

    @property
    def collection_name(self) -> str:
        return self.__collection_name

    @property
    def tg_bot_token(self) -> str:
        return self.__tg_bot_token

    def __init__(self) -> None:
        load_dotenv()  # Load environment variables from .env file

        self.__mongo_host = os.getenv('MONGO_HOST', 'localhost')
        self.__mongo_port = int(os.getenv('MONGO_PORT', 27017))
        self.__database_name = os.getenv('DATABASE_NAME', 'db')
        self.__collection_name = os.getenv('COLLECTION_NAME', 'sample_collection')
        self.__tg_bot_token = os.getenv('TG_BOT_TOKEN', '')

        if self.__tg_bot_token == "":
            self.__tg_bot_token = os.environ.get('TG_BOT_TOKEN')
