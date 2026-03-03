from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.model_training import ModelTrainer
from src.Text_Summarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        self.config=ConfigurationManager()
    
    def initiate_model_training(self):
        try:
            model_training_config=self.config.get_model_training_config()
            model_trainer=ModelTrainer(config=model_training_config)
            model_trainer.train()
        except Exception as e:
            logger.error(f"Error in Model Training: {e}")
            raise e