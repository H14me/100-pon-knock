#coding:utf-8

text1 = u"パトカー"
text2 = u"タクシー"

#最適解
ans = [t1 + t2 for t1, t2 in zip(text1,text2)]
print "".join(ans) #sep.join(seq) 区切り文字でseqを連結して文字列に

# ans = ""
# for t1,t2 in zip(text1,text2): #zipはtext1とtext2から交互に順に文字をとってくる
# 	ans += t1 + t2

# print ans 


# t = text1[0] + text2[0] + text1[1] + text2[1] + text1[2] + text2[2] + text1[3] + text2[3] 
# print t 