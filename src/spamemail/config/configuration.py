from spamemail import logging
from spamemail.utils.common import create_directories, read_yaml
from spamemail.constants import *
from spamemail.entity import (
    DataIngestionConfig,
    DataValidationConfig,
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