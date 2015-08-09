# 途中

def ngram(text, n):
    results = []
    if len(text) >= n:
        for i in range(len(text)-n+1):
            results.append(text[i:i+n])
    return results

text = "I am an NLPer"
for v in ngram(text, 2):
    print v