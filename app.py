from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import os,sys

if __name__=="__main__":
    try:
        logging.info("Starting the ML Project")
        a=1/0
    except Exception as e:
        logging.info("Exception occured")
        raise CustomException(e,sys)
