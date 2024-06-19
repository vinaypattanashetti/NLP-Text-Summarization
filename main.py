""""
Created on June 14, 2024
@ Author: Vinay Pattanashetti"""

from textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarization.logging import logger

STAGE_NAME = 'Data_ingestion_stage'

try:
    logger.info(f">>>>>>>>Stage {STAGE_NAME} started<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>{STAGE_NAME} completed successfully<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Data_validation_stage'

try:
    logger.info(f">>>>>>>>Stage {STAGE_NAME} started<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>{STAGE_NAME} completed successfully<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e 