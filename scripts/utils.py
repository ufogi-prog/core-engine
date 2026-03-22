# utils.py

import os
import logging
import inspect

def get_current_function_name():
    """Return the name of the current function."""
    return inspect.stack()[1].function

def create_directory(path):
    """Create a directory and all its parents if they do not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def setup_logging():
    """Setup logging with a file and console handlers."""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler('core-engine.log'),
            logging.StreamHandler()
        ]
    )