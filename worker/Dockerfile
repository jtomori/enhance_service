FROM python:2.7.15-alpine3.7
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["rq", "worker", "-u", "redis://redis:6379"]