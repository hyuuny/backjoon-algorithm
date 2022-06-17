words = []
while True:
    words.append(input())
    if words[-1] == '0':
        break

for word in words[:-1]:
    reverse_word = word[::-1]
    palindrome = True

    for i in range(len(word)):
        if reverse_word[i] != word[i]:
            palindrome = False

    print('yes') if palindrome else print('no')