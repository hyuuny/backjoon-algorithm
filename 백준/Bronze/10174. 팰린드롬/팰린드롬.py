def process():
    word = input().lower()

    reversed_word = word[::-1]

    palindrome = True
    for i in range(len(word)):
        if word[i] != reversed_word[i]:
            palindrome = False

    print("Yes") if palindrome else print("No")


for _ in range(int(input())):
    process()