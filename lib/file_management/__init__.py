"""
File management
===============

Provides
    1. Make it easier to send requests to the server.
    2. Easy to manage file.
    3. Make student work more systematic.

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a reference guide, available in README.md

Available packages
---------------------
WorkEditor
    Manage data in work.json

ConfigEditor
    Create, read and check exist file config.json

SaveApiKey  
    Create, read, remove and check file taconfig.json

DirManagement
    Create and Remove directory

manage_work_file
    Manage and check student work
"""

from .config_editor import *
from .create_apikeyfile import *
from .manage_work_file import *
from .file_management_lib import *
