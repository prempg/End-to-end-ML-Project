from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation, DataTransformationConfig
import os,sys

if __name__=="__main__":
    try:
        logging.info("Starting the ML Project")
        data_ingestion=DataIngestion()
        train_data,test_data=data_ingestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        data_transformation.initiate_data_transormation(train_data,test_data)
    except Exception as e:
        logging.info("Exception occured")
        raise CustomException(e,sys)
