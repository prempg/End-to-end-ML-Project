from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
import os,sys

if __name__=="__main__":
    try:
        logging.info("Starting the ML Project")
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Exception occured")
        raise CustomException(e,sys)
