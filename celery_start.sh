sudo docker run -d  -p 5672:5672 -p 15672:15672 7601e834fa1414
celery -A tasks1 worker -B --loglevel=info
