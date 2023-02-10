FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r /app/requirements.txt

ADD swagger_client /app/swagger_client
ADD mta /app/mta
COPY config.json config.json
COPY conftest.py conftest.py
COPY pytest.ini pytest.ini
ENTRYPOINT [ "python3.9", "-m" , "pytest" , "-v", "--tc-file=config.json", "--tc-format=json"]
