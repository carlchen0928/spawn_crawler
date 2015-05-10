__author__ = 'yiyuchen'
import Logging
import lxml.html as lht

'''
base ref: relative url convert to absolute address
tags    : expected url tags
'''
def extract_links(html, base_ref, tags=[]):
	if not html.strip():
		return
	link_list = []
	try:
		doc = H.document_fromstring(html)
	except Exception, e:
		Log
	pass


def extract(extract_queue):
	task = extract_queue.get()