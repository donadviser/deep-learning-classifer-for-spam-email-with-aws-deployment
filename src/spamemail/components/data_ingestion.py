import os
import sys
import urllib.request as request
import zipfile
from pathlib import Path
from spamemail import logging
from spamemail import CustomException
from spamemail.utils.common import get_size
from spamemail.entity import (
    DataIngestionConfig,
)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self) -> None:
        """Downloads a file from a specified URL if it does not already exist locally.
        
        Raises:
            CustomException: If there is an error during the download process.
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file,
                )
                logging.info(f"Downloaded file: {filename} with the info: {headers}")

            else:
                logging.info(f"File already exists: {self.config.local_data_file} with size: {Path(self.config.local_data_file)}")
        except Exception as e:
            raise CustomException(e, sys)

    def extract_zip_file(self) -> None:
        """
        Extracts the downloaded zip file.
        """
        if self.config.local_data_file.endswith(".zip"):
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
                logging.info(f"Extracted files from zip file: {self.config.local_data_file}")

        else:
            raise CustomException(f"Invalid file format: {self.config.local_data_file}")
        