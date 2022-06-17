n = int(input())

for i in range(n):
    str = input().split()

    for word in str:
        print(''.join(reversed(word)), end=" ")
        
    print()
