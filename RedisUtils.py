__author__ = 'yiyu'
import redis
import settings
import Task

pool = redis.ConnectionPool(host=settings.REDIS_HOST,
                            port=settings.REDIS_PORT)
r = redis.Redis(connection_pool=pool)


def get_task():
	"""

	:rtype : object
	"""
	obj_str = r.blpop(settings.WORKER_NAME)
	return Task.deserialize(obj_str)