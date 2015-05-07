__author__ = 'yiyu'
import redis
import settings

pool = redis.ConnectionPool(host=settings.REDIS_HOST,
                            port=settings.REDIS_PORT)
r = redis.Redis(connection_pool=pool)


def get_url():
	return r.blpop(settings.WORKER_NAME)