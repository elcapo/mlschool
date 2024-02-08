import pathlib
import pytest

from mlschool import Settings, Session, PreProcessingStep
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.parameters import ParameterString
from sagemaker.workflow.steps import CacheConfig, ProcessingStep

@pytest.mark.filterwarnings('ignore::UserWarning')
def test_pre_processing_step():
    tests_folder = pathlib.Path(__file__).parent.resolve()
    settings = Settings(env_file=tests_folder.joinpath("../env.tests"))
    session = Session(settings=settings)
    pre_processing_step = PreProcessingStep(session=session)

    dataset_location = pre_processing_step.getDatasetLocation()
    assert isinstance(dataset_location, ParameterString)

    cache_config = pre_processing_step.getCacheConfig()
    assert isinstance(cache_config, CacheConfig)

    settings = pre_processing_step.getSettings()
    assert isinstance(settings, Settings)

    processor = pre_processing_step.getProcessor()
    assert isinstance(processor, SKLearnProcessor)

    processing_step = pre_processing_step.getProcessingStep()
    assert isinstance(processing_step, ProcessingStep)
