word = input().upper()
words = list(set(word))
word_count = []

for i in words:
    word_count.append(word.count(i))

if word_count.count(max(word_count)) > 1:
    print('?')
else:
    max_idx = word_count.index(max(word_count))
    print(words[max_idx])
