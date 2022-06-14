def sorted_words(words):
    words = list(set(words)) # 중복 제거
    # 1 : 길이순, 2: 오름차순
    words.sort()
    words.sort(key = lambda x:len(x))

    for i in words: # 하나씩 출력
      print(i) 


n = int(input())
words = [input() for _ in range(n)]
sorted_words(words)