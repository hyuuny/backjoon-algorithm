def line_up(names):
    if names == sorted(names):
        print("INCREASING")
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")


names = [input() for _ in range(int(input()))]
line_up(names)
