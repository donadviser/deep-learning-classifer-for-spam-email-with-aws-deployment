import sys
import pandas as pd
from pathlib import Path
from typing import List, Union

from spamemail import logging
from spamemail import CustomException

from spamemail.entity import (
    DataValidationConfig,
)


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self) -> bool:
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

        data_dir = Path(self.config.unzip_data_dir)
        schema_keys = list(self.config.all_schema.keys())

        try:
            # Read data using pandas
            data = pd.read_csv(data_dir)
            all_cols = list(data.columns)

            logging.info(f"All columns in the file: {all_cols}")
            logging.info(f"Schema keys: {schema_keys}")

            # Validate all columns are present in the schema
            validation_status = all(col in schema_keys for col in all_cols)

            # Write validation status to file atomically (avoid partial writes)
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logging.info(f"Validation status: {validation_status}")
            return validation_status

        except pd.errors.ParserError as e:
            # Handle specific pandas parsing errors
            raise CustomException(f"Error parsing data file: {e}", sys)
        except FileNotFoundError as e:
            # Handle file not found error
            raise CustomException(f"Data file not found: {e}", sys)
        except Exception as e:
            # Catch other exceptions for robustness
            raise CustomException(f"Unexpected error during validation: {e}", sys)
