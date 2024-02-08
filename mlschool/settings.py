from dotenv import load_dotenv
import logging
import json
import os
from pathlib import Path
import sys

class Settings:
    def __init__(self, local_mode=True):
        load_dotenv()

        self.code_folder = Path("code")
        self.code_folder.mkdir(parents=True, exist_ok=True)

        self.inference_code_folder = self.code_folder.joinpath("inference")
        self.inference_code_folder.mkdir(parents=True, exist_ok=True)

        sys.path.extend([f"./{self.code_folder}", f"./{self.inference_code_folder}"])

        self.data_filepath = "penguins.csv"

        self.setLoggingLevel()
        self.setMode(local_mode)
    
    def setLoggingLevel(self, logging_level=logging.ERROR):
        """By default, The SageMaker SDK logs events related to the default
        configuration using the INFO level. To prevent these from spoiling
        the output of this notebook cells, we can change the logging
        level to ERROR instead."""
        logging.getLogger("sagemaker.config").setLevel(logging_level)

    def setMode(self, local_mode=True):
        self.local_mode = local_mode
    
    def isLocal(self):
        return self.local_mode
    
    def getAwsBucket(self):
        return os.environ["BUCKET"]
    
    def getAwsRole(self):
        return os.environ["ROLE"]
    
    def getAwsLocation(self):
        bucket = self.getAwsBucket()
        return f"s3://{bucket}/penguins"
    
    def getAwsDomainId(self):
        return os.environ["DOMAIN_ID"]

    def getAwsUserProfile(self):
        return os.environ["USER_PROFILE"]

    def isAppleArchitecture(self):
        architecture = subprocess.check_output(["uname", "-m"]).decode('ascii').strip()
        return architecture == "arm64"
