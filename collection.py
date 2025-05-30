from collections import Counter

str = "Rohit Kumar Dubey is a good boy. He is trying hard to get a placement. He is very polite. He is very humble."

words = str.split()

word_count = Counter(words)

print(word_count['is']) 


