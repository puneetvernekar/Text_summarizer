from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.data_transformation import DataTransformation
from src.Text_Summarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        self.config=ConfigurationManager()
    
    def initiate_data_transformation(self):
        try:
            data_transformation_config=self.config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.error(f"Error in Data Transformation: {e}")
            raise e