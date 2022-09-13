def croatia_alphabet(word):
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for i in croatia:
        count = word.count(i)
        if count > 0:
            word = word.replace(i, "*")

    return len(word)


print(croatia_alphabet(input().rstrip()))