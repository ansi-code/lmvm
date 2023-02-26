FROM python:3.8

COPY ./ /app/
WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "src/main.py" ]

# USAGE EXAMPLE
# docker build . --tag lmvm --progress=plain --no-cache
# docker run --rm "lmvm"