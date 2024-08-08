from spamemail import logging
from spamemail.utils.common import create_directories, read_yaml
from spamemail.constants import *
from spamemail.entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    )


class ConfigurationManager:
    def __init__(
            self,
            config_filepath: Path = CONFIG_FILE_PATH,
            params_filepath: Path = PARAMS_FILE_PATH,
            schema_filepath: Path = SCHEMA_FILE_PATH,
        ):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artefacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Retrieves and validates data ingestion configuration.

        Creates necessary directories if they don't exist.

        Args:
            self: The object containing the configuration.

        Returns:
            DataIngestionConfig: The parsed configuration.

        Raises:
            ValueError: If required configuration values are missing or invalid.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir,
        )
        logging.info(f"Data ingestion configuration loaded: {data_ingestion_config}")
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS + self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema,
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.simple_nn
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            x_test_path= config.x_test_path,
            x_train_path= config.x_train_path,
            y_test_path= config.y_test_path,
            y_train_path= config.y_train_path,
            model_name= config.model_name,
            optimizer= params.optimizer,
            loss= params.loss,
            metrics= params.metrics,            
            target_column= schema.Category,
            model_figure_path = config.model_figure_path
        )

        return model_trainer_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_path = config.model_path,
            target_column = schema.Category,
            metrics_json_file = config.metrics_json_file,
            metric_figure_path = config.metric_figure_path,
        )

        return model_evaluation_config