def solution(s):
    alphabets = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, alphabet in enumerate(alphabets):
        if alphabet in s:
            # 입력받은 문자열의 단어를 숫자로 바꾼다. (one -> str(1))
            s = s.replace(alphabet, str(idx))

    return int(s)


# 테스트 코드입니다.
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))