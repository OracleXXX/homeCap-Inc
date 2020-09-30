FROM python:3.7
WORKDIR /Project/homecap

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]