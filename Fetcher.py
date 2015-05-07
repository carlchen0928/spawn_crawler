__author__ = 'yiyu'
from gevent import Greenlet
import gevent
from multiprocessing import Queue
import RedisUtils
import Logging
import HumanHeader
import requests
import settings


class Fetcher(Greenlet):
	def __init__(self, extract_queue):
		Greenlet.__init__()
		assert isinstance(extract_queue, Queue)
		self.extract_queue = extract_queue
		pass

	def _fetch(self):
		while True:
			task = RedisUtils.get_task()
			if not task:
				Logging.error('Fetcher._fetch task is None, error')
				continue
			content = self._request(task)
			task.set_content(content)
			# dispatch task into queue
			self.extract_queue.put(task)

	def _request(self, task):
		header = HumanHeader.get_header()
		try:
			Logging.info('start to crawler %s' % task.cur_url)
			if settings.TIMEOUT != 0:
				content = requests.get(task.cur_url,
				                       headers=header,
				                       stream=True,
				                       timeout=settings.TIMEOUT)
			else:
				content = requests.get(task.cur_url,
				                       headers=header,
				                       stream=True)
		except Exception, e:
			Logging.error('%s %s' % (task.cur_url, str(e)))
			return None
		return content

	def _run(self):
		self._fetch()