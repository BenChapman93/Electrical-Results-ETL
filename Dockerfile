FROM ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.2.3}


USER airflow
RUN pip install --upgrade pip

COPY requirements.txt /opt/airflow
WORKDIR /opt/airflow
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/src"