import pathlib

from mlschool import Settings, Session
from sagemaker.workflow.pipeline_context import PipelineSession, LocalPipelineSession

def test_session():
    tests_folder = pathlib.Path(__file__).parent.resolve()
    settings = Settings(env_file=tests_folder.joinpath("../env.tests"))
    session = Session(settings=settings)

    region = session.getRegion()
    assert isinstance(region, str) and len(region) > 0

    config = session.getConfig()
    assert isinstance(config, dict)
    assert "session" in config
    assert isinstance(config["session"], LocalPipelineSession) or isinstance(config["session"], PipelineSession)

    settings = session.getSettings()
    assert isinstance(settings, Settings)
