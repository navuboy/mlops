from mlProject import logger
from mlProject.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_4_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} has started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e   


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} has started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e   


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} has started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e   

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} has started <<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e   