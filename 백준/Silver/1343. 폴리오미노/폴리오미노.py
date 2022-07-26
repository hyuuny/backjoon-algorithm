def polyomino(s):
    replace_s = s.replace("XXXX", "AAAA").replace("XX", "BB")
    print(replace_s) if replace_s.count('X') == 0 else print(-1)


polyomino(input())