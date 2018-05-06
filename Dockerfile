FROM python:2.7.15-alpine3.7
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
RUN sed -e "s/REDIS_HOST = 'localhost'/REDIS_HOST = 'redis'/" \
    /usr/local/lib/python2.7/site-packages/rq_dashboard/default_settings.py > tmp && \ 
    mv tmp /usr/local/lib/python2.7/site-packages/rq_dashboard/default_settings.py
ADD service.py slow_job.py /app/
EXPOSE 5000
CMD ["python", "service.py"]