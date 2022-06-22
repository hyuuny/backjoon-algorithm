def desc_checker(arr):
    desc = True
    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            desc = False
    return "Good" if desc else "Bad"


n = list(map(int, input().split()))
print(desc_checker(n)) if len(n) > 1 else print("Good")