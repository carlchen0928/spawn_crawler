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
			url = RedisUtils.get_url()
			if not url:
				Logging.error('Fetcher._fetch url is None, error')
				continue
			content = self._request(url)
			pass
		pass

	def _request(self, url):
		header = HumanHeader.get_header()
		try:
			Logging.info('start to crawler %s' % url)
			if settings.TIMEOUT != 0:
				content = requests.get(url,
				                       headers=header,
				                       stream=True,
				                       timeout=settings.TIMEOUT)
			else:
				content = requests.get(url,
				                       headers=header,
				                       stream=True)
		except Exception, e:
			Logging.error('%s %s' % (url, str(e)))
			return None
		return content


	def _run(self):
		self._fetch()