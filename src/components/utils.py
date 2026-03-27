# core-engine/utils.py

import logging
import os

def get_project_root() -> str:
    """Gets the root directory of the project."""
    return os.path.dirname(os.path.abspath(__file__))

def set_logger(log_file: str = None) -> logging.Logger:
    """Creates and configures a logger."""
    logger = logging.getLogger('core-engine')
    logger.setLevel(logging.DEBUG)
    
    if log_file:
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.DEBUG)
    else:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    return logger

def load_json(filename: str) -> dict:
    """Loads a JSON file into a dictionary."""
    with open(filename, 'r') as file:
        return json.load(file)

import json