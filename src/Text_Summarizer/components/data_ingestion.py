import os
import urllib.request as request
import zipfile
from src.Text_Summarizer.entity import DataIngestionConfig
from src.Text_Summarizer.logging import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from {self.config.source_URL} to {self.config.local_data_file}")
            filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"File downloaded successfully to {self.config.local_data_file}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}. Skipping download.")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

