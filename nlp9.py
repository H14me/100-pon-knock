#coding:utf-8

import random 

def typoglycemia(text):
	word_list = text.split()
	new_text = []
	for word in word_list:
		if len(word) > 4:
			middle = word[1:-1]##最初と最後以外がミドル
			random_middle = "".join(random.sample(middle,len(middle)))##middleから選ばれた長さ/文字数を元にリストを返す擬似乱数を作る
			word = "".join([word[0],random_middle,word[-1]])
		new_text.append(word)
	return " ".join(new_text)


if __name__ == "__main__":
	text = "I couldn't believe that I could actually understnd what I was reading : the pheomenal power of the human mind ."
	print typoglycemia(text)