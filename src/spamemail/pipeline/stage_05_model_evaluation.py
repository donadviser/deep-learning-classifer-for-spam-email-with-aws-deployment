import sys
from spamemail import logging
from spamemail import CustomException

from spamemail.config.configuration import ConfigurationManager
from spamemail.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Model evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self,res):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.eval(res[1],res[3])



if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelEvaluationTrainingPipeline()
        pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)