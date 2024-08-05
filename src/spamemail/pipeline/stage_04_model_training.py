import sys
from spamemail import logging
from spamemail import CustomException

from spamemail.config.configuration import ConfigurationManager
from spamemail.components.model_training import ModelTrainer


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self,res):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train_model(res[0],res[1],res[2],res[3])


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelTrainerTrainingPipeline()
        pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)