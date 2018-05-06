FROM python:2.7.15-alpine3.7
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD service.py slow_job.py /app/
EXPOSE 5000
CMD ["python", "service.py"]