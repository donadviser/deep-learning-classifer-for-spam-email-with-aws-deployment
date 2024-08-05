import sys
from spamemail import logging
from spamemail import CustomException
from spamemail.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from spamemail.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed successfully <<<<<<\n\nx==========x")
except CustomException as e:
    logging.error(f"An error occurred during stage {STAGE_NAME}: {str(e)}")
    raise CustomException(e, sys)


STAGE_NAME = "Data Validation Stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(f"An error occurred during stage {STAGE_NAME}: {str(e)}")
    raise CustomException(e, sys)