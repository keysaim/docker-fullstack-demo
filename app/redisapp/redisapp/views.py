from django.http import HttpResponse
import socket
import redis


def query(request):
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    value = r.get('redis_app')
    return HttpResponse('hello world from ' + socket.gethostname() + ', with value: ' + str(value))
