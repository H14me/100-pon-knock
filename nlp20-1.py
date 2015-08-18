#coding:utf-8
import json

f = ("jawiki-country.json","w")
for line in f:
	text = json.dumps(line,ensure_ascii = False)
	print line + ","