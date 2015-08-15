#coding:utf-8
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

text_split = text.translate(None,".,").split()##text.translateで(x,"y") yの文字をxに置き換え

for i in text_split:
	print len(i)

##アウトプットをリストにすべし