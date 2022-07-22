from enum import Enum

BOT_TOKEN = "5582597592:AAEzmOjj06Td3bc5Klld60Da_bie1NTXla4"
db_file = "database_bot.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_ANSWER = "2"
    S_ENTER_LEN_PASS = "3"
    S_SYMBHOLS = "4"