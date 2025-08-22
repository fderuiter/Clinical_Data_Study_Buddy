# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.7.1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python - \
    && mv /root/.local/bin/poetry /usr/local/bin/poetry

# Copy the dependency files
COPY poetry.lock pyproject.toml /app/

# Install project dependencies
# --no-root: don't install the project itself, only dependencies
# This is done in a separate step to leverage Docker layer caching.
# Dependencies are only re-installed when pyproject.toml or poetry.lock change.
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application's source code from the host to the container
COPY . /app/

# The container will run as the root user. For a production image, you might
# want to create and switch to a non-root user. For development, this is fine.
