#install python
FROM python:3.12-slim
WORKDIR /app

#install system requirements
RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

#install requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy project
COPY . .
EXPOSE 8000

#launch Gunicorn and migration and createsuperuser
CMD python manage.py migrate --noinput && \
    python -c "from django.contrib.auth import get_user_model; User = get_user_model(); \

