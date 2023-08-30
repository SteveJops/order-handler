
FROM python:3.10-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./db-entrypoint.sh .
RUN sed -i 's/\r$//g' db-entrypoint.sh
RUN chmod +x db-entrypoint.sh

COPY ./start-entrypoint.sh .
RUN sed -i 's/\r$//g' start-entrypoint.sh
RUN chmod +x start-entrypoint.sh

COPY ./beat-entrypoint.sh .
RUN sed -i 's/\r$//g' beat-entrypoint.sh
RUN chmod +x beat-entrypoint.sh

COPY ./worker-entrypoint.sh .
RUN sed -i 's/\r$//g' worker-entrypoint.sh
RUN chmod +x worker-entrypoint.sh


# copy project
COPY . .

# because of passing the script, better to do os to aboid errors
ENTRYPOINT ["sh", "./db-entrypoint.sh"] 