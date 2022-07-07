while True:

    s = list(map(str, input().split()))
    search_word = s[0]
    word = s[1:]

    # 탐색 문자가 '#'이면 정지
    if s[0] == '#': break

    # 검색된 문자 개수(문자열은 소문자로 변경해주자!)
    word_count = " ".join(word).lower().count(search_word)

    print(search_word, word_count)