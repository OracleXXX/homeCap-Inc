FROM python:3.7



WORKDIR /Project/demo
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]