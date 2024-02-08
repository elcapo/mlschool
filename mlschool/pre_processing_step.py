from mlschool.session import Session
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.parameters import ParameterString
from sagemaker.workflow.steps import CacheConfig, ProcessingStep

class PreProcessingStep:
    def __init__(self, session: Session):
        self.session = session
    
    def getDatasetLocation(self):
        settings = self.session.getSettings()

        return ParameterString(
            name="dataset_location",
            default_value=f"{settings.getAwsLocation()}/data",
        )
    
    def getCacheConfig(self):
        return CacheConfig(enable_caching=True, expire_after="15d")
    
    def getSettings(self):
        return self.session.getSettings()
    
    def getConfig(self):
        return self.session.getConfig()

    def getProcessor(self):
        config = self.getConfig()
        settings = self.getSettings()

        return SKLearnProcessor(
            base_job_name="preprocess-data",
            framework_version="1.2-1",
            # By default, a new account doesn't have access to `ml.m5.xlarge` instances.
            # If you haven't requested a quota increase yet, you can use an
            # `ml.t3.medium` instance type instead. This will work out of the box, but
            # the Processing Job will take significantly longer than it should have.
            # To get access to `ml.m5.xlarge` instances, you can request a quota
            # increase under the Service Quotas section in your AWS account.
            instance_type=config["instance_type"],
            instance_count=1,
            role=settings.getAwsRole(),
            sagemaker_session=config["session"],
        )
    
    def getProcessingStep(self):
        processor = self.getProcessor()
        settings = self.getSettings()
        code_folder = settings.getCodeFolder()
        aws_location = settings.getAwsLocation()

        return ProcessingStep(
            name="preprocess-data",
            step_args=processor.run(
                code=f"{code_folder}/preprocessor.py",
                inputs=[
                    ProcessingInput(
                        source=self.getDatasetLocation(),
                        destination="/opt/ml/processing/input",
                    ),
                ],
                outputs=[
                    ProcessingOutput(
                        output_name="train",
                        source="/opt/ml/processing/train",
                        destination=f"{aws_location}/preprocessing/train",
                    ),
                    ProcessingOutput(
                        output_name="validation",
                        source="/opt/ml/processing/validation",
                        destination=f"{aws_location}/preprocessing/validation",
                    ),
                    ProcessingOutput(
                        output_name="test",
                        source="/opt/ml/processing/test",
                        destination=f"{aws_location}/preprocessing/test",
                    ),
                    ProcessingOutput(
                        output_name="model",
                        source="/opt/ml/processing/model",
                        destination=f"{aws_location}/preprocessing/model",
                    ),
                    ProcessingOutput(
                        output_name="train-baseline",
                        source="/opt/ml/processing/train-baseline",
                        destination=f"{aws_location}/preprocessing/train-baseline",
                    ),
                    ProcessingOutput(
                        output_name="test-baseline",
                        source="/opt/ml/processing/test-baseline",
                        destination=f"{aws_location}/preprocessing/test-baseline",
                    ),
                ],
            ),
            cache_config=self.getCacheConfig(),
        )
    
