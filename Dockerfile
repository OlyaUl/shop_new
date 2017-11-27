FROM python:3
WORKDIR /app
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
EXPOSE 8000
ENTRYPOINT python shop_cars/manage.py migrate && python shop_cars/manage.py runserver 0.0.0.0:8000