for _ in range(int(input())):
    word = list(map(str, input().rstrip().split()))
    word[0] = "god"
    print("".join(word))