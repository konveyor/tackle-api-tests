FROM python:3.9

WORKDIR /app

COPY conftest.py requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD data/ /app/data
ADD fixtures/ /app/fixtures
ADD swagger_client /app/swagger_client
ADD tests/ /app/tests
ADD utils/ /app/utils
COPY pytest.ini pytest.ini
ENTRYPOINT [ "python3.9", "-m" , "pytest" , "-v" ]
