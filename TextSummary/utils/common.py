import os
from box import Box
import yaml
from TextSummary.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, List

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """Reads yaml file and returns a Box (dictionary-like) object."""
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not isinstance(content, dict):
                raise ValueError("yaml content is not a dictionary")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return Box(content)
    except ValueError as ve:
        logger.error(f"ValueError loading yaml file: {ve}")
        raise ve
    except Exception as e:
        logger.error(f"Error loading yaml file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of a file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

# Example usage:
if __name__ == "__main__":
    yaml_path = Path("/path/to/your/yaml/file.yaml")
    try:
        yaml_data = read_yaml(yaml_path)
        # Do something with yaml_data
    except Exception as e:
        print(f"Error: {e}")
