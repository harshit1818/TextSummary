import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(module)s: %(message)s]"

# Define the directory and file for logging
log_dir = "logs"
log_path = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger
logger = logging.getLogger("TextSummaryLogger")


