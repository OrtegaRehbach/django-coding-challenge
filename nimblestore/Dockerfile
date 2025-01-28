FROM python:3.12-slim AS base

## Add https://github.com/ufoscout/docker-compose-wait to the image
COPY --from=ghcr.io/ufoscout/docker-compose-wait:latest /wait /wait


RUN apt update && apt -y install python3-pip libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 weasyprint ncat && apt clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Default command (can be overridden)
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]