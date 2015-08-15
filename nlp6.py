#coding:utf-8

if __name__ == "__main__":
	from nlp5 import chr_ngram
	text1 = "paraparaparadise"
	text2 = "paragraph"

	x = set(chr_ngram(text1,2)) ##setは集合演算しやすくするようにするやつ
	y = set(chr_ngram(text2,2))

	print "X:",x
	print "Y:",y
	print "和集合: ", x | y
	print "積集合: ", x & y
	print "差集合: ", x - y