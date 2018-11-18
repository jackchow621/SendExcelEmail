FROM python:2.7.13

MAINTAINER jackchow "jack_chow621@sina.com"

RUN pip install -r requirements.txt


CMD ["python", "/code/run.py"]
