def converter(s):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V',
             'W', 'X', 'Y', 'Z']
    caesar = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
              'Y',
              'Z', 'A', 'B', 'C']

    ans = []
    for word in s:
        index = caesar.index(word)
        ans.append(alpha[index])

    return "".join(ans)


s = input()
print(converter(s))