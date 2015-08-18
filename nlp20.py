#coding:utf-8
import json

target_country = u"イギリス"
f = open("jawiki-country.json","r")

for line in f:
	# print type(line)
	text = json.loads(line) 
	if text["title"] == target_country:
		print text["text"]
		# ans = json.dumps(text, ensure_ascii=False)##json.dumpsで日本語で出なかったら、ensure_ascii使って日本語にする

# for line in ans.split("\n"):
# 	print line

f.close()