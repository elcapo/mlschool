import boto3
import sagemaker

from mlschool.settings import Settings
from sagemaker.workflow.pipeline_context import PipelineSession, LocalPipelineSession

class Session:
    def __init__(self, settings: Settings):
        if settings.isLocal():
            self.config = {
                "session": LocalPipelineSession(default_bucket=settings.getAwsBucket()),
                "instance_type": "local",
                # We need to use a custom Docker image when we run the pipeline
                # in Local Model on an ARM64 machine.
                "image": "sagemaker-tensorflow-toolkit-local" if settings.isAppleArchitecture() else None,
            }
        else:
            self.config = {
                "session": PipelineSession(default_bucket=settings.getAwsBucket()) if not settings.isLocal() else None,
                "instance_type": "ml.m5.xlarge",
                "image": None,
            }

        self.config["framework_version"] = "2.11"
        self.config["py_version"] = "py39"
        self.settings = settings
    
    def getSagemakerClient(self):
        return boto3.client("sagemaker")

    def getIamClient(self):
        return boto3.client("iam")
    
    def getRegion(self):
        return boto3.Session().region_name
    
    def getConfig(self):
        return self.config
    
    def getSettings(self):
        return self.settings
