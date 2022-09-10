def replace_pikachu(word):
    replaced_pi = word.replace('pi', ' ')
    replaced_ka = replaced_pi.replace('ka', ' ')
    return replaced_ka.replace('chu', ' ')


answer = replace_pikachu(input())
print('YES') if answer.replace(' ', '') == '' else print('NO')