def solve(arr, reverse_arr):
    print('yes') if arr == reverse_arr else print('no')


while True:
    word = list(map(int, input()))
    if word[0] == 0: break
    solve(word, word[::-1])