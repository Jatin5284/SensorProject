import logging
import os # process to get the current working directory
from datetime import datetime

# 1) Create a file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y"_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "Logs" ,LOG_FILE) # create a logs folder in the current working directory and getcwd() to get the current working directory


# 2) Create a directory
os.makedirs(logs_path , exist_ok=True) 


# 3) Create file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] - %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    level = logging.INFO # set the level of logging to INFO
)