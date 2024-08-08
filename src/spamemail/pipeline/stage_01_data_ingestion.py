import sys
from spamemail import logging
from spamemail import CustomException

from spamemail.config.configuration import ConfigurationManager
from spamemail.components.data_ingestion import DataIngestion

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logging.info(f'Starting {STAGE_NAME} pipeline...')
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logging.info(f'Completed {STAGE_NAME} pipeline successfully.')
    except CustomException as e:
        raise CustomException(e, sys)
    