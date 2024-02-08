from dotenv import load_dotenv
from mlschool import Settings
import pytest

@pytest.fixture
def setup_data():
    load_dotenv("env.tests")

def test_settings(setup_data):
    settings = Settings()
    assert settings.isLocal()
    assert settings.getAwsBucket() == "my-aws-custom-mlschool-bucket"
    assert settings.getAwsRole() == "arn:aws:iam::999999999999:role/service-role/AmazonSageMaker-ExecutionRole-20240101T000000"
    assert settings.getAwsDomainId() == "d-my-aws-domain-id"
    assert settings.getAwsUserProfile() == "my-aws-custom-user"