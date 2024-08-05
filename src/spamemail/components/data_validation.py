import sys
import pandas as pd
from spamemail import logging
from spamemail import CustomException

from spamemail.entity import (
    DataValidationConfig,
)


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        """Validates if all columns in the data file match the expected schema.

        Reads the data file using pandas, checks if all columns are present in the
        configuration schema, and writes the validation status to a file.

        Args:
            self: The object containing the configuration.

        Returns:
            bool: True if all columns are valid, False otherwise.

        Raises:
            CustomException: If an error occurs while reading the data file or
                            writing the validation status.
        """
        try:

            # Read data using pandas
        data = pd.read_csv(data_dir)
        all_cols = list(data.columns)

        logger.info(f"All columns in the file: {all_cols}")
        logger.info(f"Schema keys: {schema_keys}")

        # Validate all columns are present in the schema
        validation_status = all(col in schema_keys for col in all_cols)

        # Write validation status to file atomically (avoid partial writes)
        with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation status: {validation_status}")

        logger.info(f"Validation status: {validation_status}")
        return validation_status
    
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            logging.info(f"All columns in the file: {all_cols}")

            all_schema = self.config.all_schema.keys()
            logging.info(f"Schema keys: {all_schema}")
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            logging.info(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise CustomException(e, sys)