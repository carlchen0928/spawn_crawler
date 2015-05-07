__author__ = 'yiyu'

accept = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8']
user_agent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
              'like Gecko) Chrome/32.0.1700.76 Safari/537.36']
encoding = ['gzip,deflate,sdch']


def get_header():
	return {'Accept': accept[0],'User-Agent': user_agent[0], 'Accept-Encoding': encoding[0]}