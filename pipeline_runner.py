import sys

from mlschool import Pipeline, PreProcessingStep, Session, Settings

def pipeline_run(local_mode=True):
    settings = Settings(local_mode=local_mode)
    session = Session(settings=settings)
    pre_processing_step = PreProcessingStep(session=session)
    pipeline = Pipeline(pre_processing_step=pre_processing_step)
    pipeline.save()
    pipeline.start()

if __name__ == "__main__":
    local_mode = not "--remote" in sys.argv
    pipeline_run(local_mode)
