from mlschool.pre_processing_step import PreProcessingStep
from sagemaker.workflow.pipeline import Pipeline as SageMakerPipeline
from sagemaker.workflow.pipeline_definition_config import PipelineDefinitionConfig

class Pipeline:
    def __init__(self, pre_processing_step: PreProcessingStep):
        self.pre_processing_step = pre_processing_step

    def getConfig(self):
        return self.pre_processing_step.getConfig()

    def getSettings(self):
        return self.pre_processing_step.getSettings()
    
    def getDatasetLocation(self):
        return self.pre_processing_step.getDatasetLocation()
    
    def getProcessingStep(self):
        return self.pre_processing_step.getProcessingStep()
    
    def getPipeline(self):
        config = self.getConfig()

        return SageMakerPipeline(
            name="session1-pipeline",
            parameters=[self.getDatasetLocation()],
            steps=[self.getProcessingStep()],
            pipeline_definition_config=PipelineDefinitionConfig(use_custom_job_prefix=True),
            sagemaker_session=config["session"],
        )
    
    def save(self):
        settings = self.getSettings()
        pipeline = self.getPipeline()
        pipeline.upsert(role_arn=settings.getAwsRole())

    def start(self):
        pipeline = self.getPipeline()
        pipeline.start()
