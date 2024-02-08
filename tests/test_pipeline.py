import pathlib
import pytest

from mlschool import Settings, Session, PreProcessingStep, Pipeline
from sagemaker.workflow.pipeline import Pipeline as SageMakerPipeline
from sagemaker.workflow.pipeline_definition_config import PipelineDefinitionConfig

@pytest.mark.filterwarnings('ignore::UserWarning')
def test_pipeline():
    tests_folder = pathlib.Path(__file__).parent.resolve()
    settings = Settings(env_file=tests_folder.joinpath("../env.tests"))
    session = Session(settings=settings)
    pre_processing_step = PreProcessingStep(session=session)
    pipeline = Pipeline(pre_processing_step=pre_processing_step)

    sagemaker_pipeline = pipeline.getPipeline()
    assert isinstance(sagemaker_pipeline, SageMakerPipeline)
