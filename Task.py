__author__ = 'yiyu'

import datetime
import pickle
import Logging


class Task:
	def __init__(self, max_depth, parent_url, webkit=False):
		self.max_depth = max_depth
		self.cur_depth = 0
		self.parent_url = parent_url
		self.cur_url = parent_url
		self.crawl_time = datetime.datetime()
		self.webkit = webkit

	def increase(self):
		self.cur_depth += 1

	def set_time(self, t):
		self.crawl_time = t


def serialize(obj):
	try:
		return pickle.dumps(obj)
	except Exception, e:
		Logging.error('serialize error %s-%s' % (obj.cur_url, str(e)))
		return None


def deserialize(obj_str):
	try:
		return Task(pickle.loads(obj_str))
	except Exception, e:
		Logging.error('serialize error %s-%s' % (obj_str, str(e)))
		return None