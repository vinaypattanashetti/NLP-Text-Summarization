""""
Created on June 14, 2024
@ Author: Vinay Pattanashetti"""

import os
from box.exceptions import BoxValueError
import yaml
from textsummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Reads the yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (str): Path like input to the yaml file
    
    Raises:
        ValueError: if the yaml file is empty
        e: empty yaml file
    
    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml}loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose= True):
    """
    Creates the list of directories
    Args:
        path_to_directories (list): list of path to directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}for the file")

@ensure_annotations
def get_size(path:Path) ->str:
    """
    get the size of the file in KB
    
    Args:
        path (Path): path to the file
    
    Returns:
        str: size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}KB"
