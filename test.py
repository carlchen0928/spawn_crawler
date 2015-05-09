__author__ = 'yiyuchen'

import grequests
import time

start = time.time()

urls = ['http://www.csdn.net/'] * 2000

rs = (grequests.get(u) for u in urls)

t = grequests.map(rs)

print time.time() - start