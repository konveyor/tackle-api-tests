FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD swagger_client /app/swagger_client
ADD tests/ /app/tests
ADD utils/ /app/utils
COPY pytest.ini pytest.ini
ENTRYPOINT [ "python3.9", "-m" , "pytest" , "tests" ]
