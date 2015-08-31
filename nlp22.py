#coding:utf-8
import json
import re 

target_country = u"イギリス"
f = open("jawiki-country.json","r")

for line in f:
	text = json.loads(line) 
	if text["title"] == target_country:
		e_text = text["text"]

for line in e_text.splitlines():
	if line.find("Category") >= 0:
		name = re.split(":", line)[1]
		print name.replace("*","").replace("]","")


		

f.close()