def remove_vowel(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    ans = []
    for word in s:
        if word not in vowel:
            ans.append(word)

    return "".join(ans)


def check_first_and_last(s1_start, s2_start, s1_end, s2_end):
    return s1_start == s2_start and s1_end == s2_end


def check_word(s):
    dict = {}
    for s in s:
        if s not in dict:
            dict.setdefault(s, 0)
        dict[s] += 1
    return dict


n = int(input())
str1 = input()
str2 = input()

flag = True
# 한 단어를 재배열해 다른 단어를 만들 수 있어야 한다.
if not check_word(str1) == check_word(str2): flag = False

# 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
if not check_first_and_last(str1[0], str2[0], str1[-1], str2[-1]): flag = False

# 각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다.
if not remove_vowel(str1) == remove_vowel(str2): flag = False

print('YES') if flag else print('NO')
