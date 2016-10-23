#!/usr/bin/python
import os
import time
import datetime
import random

first_access_since = int(os.getenv('FIRST_ACCESS_SINCE', 31536000))
last_access_since = int(os.getenv('LAST_ACCESS_SINCE', 0))
min_shift = int(os.getenv('MIN_SHIFT', 30))
max_shift = int(os.getenv('MAX_SHIFT', 30000))
min_mod_linear = int(os.getenv('MIN_MOD_LINEAR', 0))
max_mod_linear = int(os.getenv('MAX_MOD_LINEAR', 0))
min_mod_factor = float(os.getenv('MIN_MOD_FACTOR', 1))
max_mod_factor = float(os.getenv('MAX_MOD_FACTOR', 1))

f = open('access_log.log','w')

ips=["123.221.14.56","16.180.70.237","10.182.189.79","218.193.16.244","198.122.118.164","114.214.178.92","233.192.62.103","244.157.45.12","81.73.150.239","237.43.24.118"]
referers=["-","http://www.shoppingsite.com","http://shoptoplist.com/top_shops","http://productreviews.com","http://searchengine.com"]
resources=["/section1","/section2","/section3","/section4","/section5","/section6","/section7","/section8"]
useragents=["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36","Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25","Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201","Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0","Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"]

now = datetime.datetime.now()
otime = now - datetime.timedelta(seconds=first_access_since)
maxtime = now - datetime.timedelta(seconds=last_access_since)

while otime < maxtime:
	increment = datetime.timedelta(seconds=random.randint(min_shift,max_shift))
	otime += increment
	uri = random.choice(resources)
	if uri.find("Store")>0:
		uri += `random.randint(1000,1500)`
	ip = random.choice(ips)
	useragent = random.choice(useragents)
	referer = random.choice(referers)
	f.write('%s - - [%s] "GET %s HTTP/1.0" 200 %s "%s" "%s"\n' % (random.choice(ips),otime.strftime('%d/%b/%Y:%H:%M:%S %z'),uri,random.randint(2000,5000),referer,useragent))
	temp_min_shift = (min_shift + min_mod_linear) * min_mod_factor
	temp_max_shift = (max_shift + max_mod_linear) * max_mod_factor
	if temp_min_shift < temp_max_shift:
		min_shift = int(temp_min_shift)
	if temp_max_shift > temp_min_shift:
		max_shift = int(temp_max_shift)
