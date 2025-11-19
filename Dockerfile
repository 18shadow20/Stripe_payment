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
CMD ["sh", "-c", "\
python manage.py migrate && \
python -c \"import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','Stripe_payment.settings'); import django; django.setup(); \
from django.contrib.auth import get_user_model; User = get_user_model(); \
User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin','password123')\" && \
gunicorn Stripe_payment.wsgi:application --bind 0.0.0.0:$PORT"]



