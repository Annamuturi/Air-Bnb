#!/usr/bin/python3
"""
This script initializes the models package with the appropriate storage engine
based on the value of the HBNB_TYPE_STORAGE environment variable.
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

def initialize_storage():
    storage_t = getenv("HBNB_TYPE_STORAGE")
    if storage_t == "db":
        return DBStorage()
    else:
        return FileStorage()

def main():
    storage = initialize_storage()
    storage.reload()

if __name__ == "__main__":
    main()

