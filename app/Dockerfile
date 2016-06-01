FROM django
COPY ./redisapp /data/redisapp
WORKDIR /data/redisapp
ENV https_proxy=http://proxy-rtp-1.cisco.com:80/
RUN pip install redis
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py", "runserver"]
CMD ["0.0.0.0:8080"]

