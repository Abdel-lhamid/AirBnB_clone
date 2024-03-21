#!/usr/bin/python3
"""import file_storage and call reload to initiate stored data"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
