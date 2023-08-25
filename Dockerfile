FROM python:3.9.17-slim-bullseye as python

ARG BUILD_ENVIRONMENT=local

ENV PYTHONFAULTHANDLER=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random

# Install apt packages
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  build-essential \
  curl \
  git \
  libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


ARG APP_HOME=/app

WORKDIR ${APP_HOME}

# Copy requirements
COPY requirements.txt ${APP_HOME}

# Install python deps via requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy start script and make it executable
COPY ./docker/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy application code to WORKDIR
COPY . ${APP_HOME}
