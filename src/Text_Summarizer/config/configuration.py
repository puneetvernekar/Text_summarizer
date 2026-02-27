from src.Text_Summarizer.constants import CONFIG_FILE_PATH
from src.Text_Summarizer.utils.common import read_yaml, create_directories
from src.Text_Summarizer.entity import DataIngestionConfig
from src.Text_Summarizer.logging import logger

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config = read_yaml(config_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            data_ingestion_config = self.config.data_ingestion
            create_directories([data_ingestion_config.root_dir])
            return DataIngestionConfig(
                root_dir=data_ingestion_config.root_dir,
                source_URL=data_ingestion_config.source_URL,
                local_data_file=data_ingestion_config.local_data_file,
                unzip_dir=data_ingestion_config.unzip_dir
            )
        except Exception as e:
            raise e