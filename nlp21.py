#coding:utf-8
import json

target_country = u"イギリス"
f = open("jawiki-country.json","r")

for line in f:
	text = json.loads(line) 
	if text["title"] == target_country:
		e_text = text["text"]

for line in e_text.splitlines():
	if line.find("Category") >= 0:
		print line
		

f.close()