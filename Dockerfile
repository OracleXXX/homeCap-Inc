FROM python:3.7

FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]