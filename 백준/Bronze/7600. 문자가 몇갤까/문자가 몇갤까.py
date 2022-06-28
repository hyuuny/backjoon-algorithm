while True:
    s = input().upper().replace(" ", "")

    if s == '#': break

    answer = []
    for word in s:
        if 65 <= ord(word) <= 90 and word not in answer:
            answer.append(word)

    print(len(answer))