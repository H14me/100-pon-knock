#coding:utf-8

def chipher(text):
	next_text = ""
	for t in text:
		if t.islower(): #大小文字の区別がある文字が全て小文字かどうかの判定
			t = chr(219 - ord(t)) #ord=unicodeポイントなるもの　chr()の逆を入れることで反転させる
		next_text += t
	return next_text


if __name__ == "__main__":
	text = "Hello World"
	ango = chipher(text)
	print ango
	hukugo = chipher(ango)
	print hukugo 