#coding:utf-8
import json

target_country = u"イギリス"
f = open("jawiki-country.json","r")

for line in f:
	text = json.loads(line) 
	if text["title"] == target_country:
		e_text = text["text"]

for line in e_text.splitlines():
	if line.count("====") > 0:
		print u"レベル１" + u"セクション:" + line.replace("=","")
	elif line.count("===") > 0:
		print u"レベル2" + u"セクション:" + line.replace("=","")
	elif line.count("==") > 0:
		print u"レベル3" + u"セクション:" + line.replace("=","")
		

f.close()