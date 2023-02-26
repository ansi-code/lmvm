FROM python:3.8

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "src/main.py" ]