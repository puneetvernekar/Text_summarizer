from src.Text_Summarizer.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.Text_Summarizer.utils.common import read_yaml, create_directories
from src.Text_Summarizer.entity import DataIngestionConfig, DataTransformationConfig, ModelEvaluationConfig,ModelTrainingConfig
from src.Text_Summarizer.logging import logger

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
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
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation
        create_directories([config.root_dir])
        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
    
    def get_model_training_config(self)->ModelTrainingConfig:
        config=self.config.model_trainer
        params=self.params.TrainingArguments
        create_directories([config.root_dir])
        return ModelTrainingConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps,
            learning_rate=params.learning_rate
        )
    
    def get_model_evaluation_config(self):
        config=self.config.model_evaluation
        create_directories([config.root_dir])
        return ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name=config.metric_file_name
        )
    