import sys
from pathlib import Path
from spamemail import logging
from spamemail import CustomException

from spamemail.config.configuration import ConfigurationManager
from spamemail.components.data_transformation import DataTransformation


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            validation_status_file = data_validation_config.STATUS_FILE

            print(f"{validation_status_file=}")

            with open(Path(validation_status_file), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                res = data_transformation.Data_transformation()
                logging.info("data_transformation is completed successfully")
                return res
            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataTransformationTrainingPipeline()
        pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)