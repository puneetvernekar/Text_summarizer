from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.data_ingestion import DataIngestion
from src.Text_Summarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        self.config=ConfigurationManager()
    
    def initiate_data_ingestion(self):
        try:
            data_ingestion_config=self.config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.error(f"Error in Data Ingestion: {e}")
            raise e