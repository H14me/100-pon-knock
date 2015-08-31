#coding:utf-8
import json

target_country = u"イギリス"
f = open("jawiki-country.json","r")

for line in f:
	# print type(line)
	text = json.loads(line) 
	if text["title"] == target_country:
		print text["text"]
		

f.close()