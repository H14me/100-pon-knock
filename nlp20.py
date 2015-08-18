#coding:utf-8
import json

target_country = u"イギリス"
f = open("jawiki-country.json","r")
t = open("nlp20.txt","w")

for line in f:
	text = json.loads(line) 
	if text["title"] == target_country:
		ans = json.dumps(text, ensure_ascii=False)##json.dumpsで日本語で出なかったら、ensure_ascii使って日本語にする

print >> t,ans.encode("utf-8")

open t 
f.close()