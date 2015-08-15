#coding:utf-8

def word_ngram(str,n): ##nにすることであとからも使えるようにする
	word_list = str.split()
	word_gram = [word_list[i:i+n] for i in range(len(word_list)-(n-1))]
	return word_gram

def chr_ngram(str,n):
	string = str.replace(" ","")##スペース消す
	chr_gram = [string[i:i+n] for i in range(len(string)-(n-1))]
	return chr_gram

if __name__ == '__main__': ## 今回は以下の作業を実行するものの、importしたときは実行されないってやつ
	str = "I am an NLPer"
	for w in word_ngram(str,2):
		print w 
	for s in chr_ngram(str,2):
		print s	



# def ngram(text, n):
#     results = []
#     if len(text) >= n:
#         for i in range(len(text)-n+1):
#             results.append(text[i:i+n])
#     return results

# text = "I am an NLPer"
# for v in ngram(text, 2):
#     print v