from housing.constant import CONFIG_FILE_PATH, CURRENT_TIME_STAMP
from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig, DataTransformationConfig, ModelEvaluationConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig





class Configuration:

    def __init__(self,
        config_file_path:str=CONFIG_FILE_PATH,
        current_time_stamp:str=CURRENT_TIME_STAMP) -> None:
        pass

    def get_data_ingestion_congif(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self)-> DataTransformationConfig:
        pass

    def get_data_model_trainer_config(self) -> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_traning_pipeline_config(self) -> TrainingPipelineConfig:
        pass
