from src.Text_Summarizer.pipeline.pipeline_data_ingestion import DataIngestionTrainingPipeline
from src.Text_Summarizer.logging import logger

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f"Error in stage {STAGE_NAME}: {e}")
    raise e
