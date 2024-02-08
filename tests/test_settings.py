import pathlib
import pytest

from mlschool import Settings

def test_settings():
    project_folder = pathlib.Path(__file__).parent.parent.resolve()
    env_file = project_folder.joinpath("env.tests")
    print("env_file", env_file)
    settings = Settings(env_file=env_file)
    assert settings.isLocal()
    assert settings.getAwsBucket() == "my-aws-custom-mlschool-bucket"
    assert settings.getAwsRole() == "arn:aws:iam::999999999999:role/service-role/AmazonSageMaker-ExecutionRole-20240101T000000"
    assert settings.getAwsDomainId() == "d-my-aws-domain-id"
    assert settings.getAwsUserProfile() == "my-aws-custom-user"