#!/usr/bin/python3
""" This module Initialize models """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
