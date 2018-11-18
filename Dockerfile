FROM python:3.6.5

MAINTAINER jackchow "jack_chow621@sina.com"

RUN pip install -r requirements.txt


CMD ["python", "/code/run.py"]
