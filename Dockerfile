FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY pyproject.toml ./
RUN pip install --no-cache-dir .[dev]

# Copy project files
COPY . .

# Make entrypoint executable
RUN chmod +x scripts/entrypoint.sh

# Create a non-root user
RUN adduser --disabled-password --gecos '' myuser && chown -R myuser /app
USER myuser

ENTRYPOINT ["scripts/entrypoint.sh"]
