import pathlib
import pytest

from mlschool import Settings, Session

def test_session():
    tests_folder = pathlib.Path(__file__).parent.resolve()
    settings = Settings(env_file=tests_folder.joinpath("../env.tests"))
    session = Session(settings=settings)
    region = session.getRegion()
    assert isinstance(region, str) and len(region) > 0
