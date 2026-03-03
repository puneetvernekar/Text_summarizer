from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForSeq2Seq
from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.entity import ModelTrainingConfig
import torch
import os
from datasets import DatasetDict, load_from_disk

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        device="cuda" if torch.cuda.is_available() else "cpu"
        self.model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        seq2seq_data_collator=DataCollatorForSeq2Seq(tokenizer=self.tokenizer,model=self.model_pegasus)
        dataset_samsum_pt=load_from_disk(self.config.data_path)
        assert isinstance(dataset_samsum_pt, DatasetDict)
        training_args=TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            learning_rate=self.config.learning_rate
        )
        trainer=Trainer(
            model=self.model_pegasus,
            args=training_args,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"],
            data_collator=seq2seq_data_collator
        )
        trainer.train()

        self.model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus_samsum_model"))
        self.tokenizer.save_pretrained(os.path.join(self.config.root_dir,"pegasus_samsum_tokenizer"))