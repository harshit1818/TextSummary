import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the project name and the list of files to create
project_name = "TextSummary"

list_of_files = [
    "github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Create each file and its directories
for filepath in list_of_files:
    file_path = Path(filepath)
    file_dir = file_path.parent

    if not file_dir.exists():
        logging.info(f"Creating directory: {file_dir}")
        os.makedirs(file_dir, exist_ok=True)
    
    if not file_path.exists():
        logging.info(f"Creating file: {file_path}")
        file_path.touch()
    else:
        logging.info(f"File already exists: {file_path}")
