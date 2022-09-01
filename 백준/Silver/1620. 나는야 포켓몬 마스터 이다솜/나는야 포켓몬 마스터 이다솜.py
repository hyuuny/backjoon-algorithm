import sys


def pokemon_master(n, m):
    pokemon = {}
    number_pokemon = {}
    for i in range(1, n + 1):
        name = sys.stdin.readline().rstrip()
        pokemon[name] = pokemon.setdefault(name, i)
        number_pokemon[i] = pokemon.setdefault(i, name)

    for i in range(m):
        name = sys.stdin.readline().rstrip()
        if name.isnumeric():
            print(number_pokemon[int(name)])
        else:
            print(pokemon[name])


n, m = map(int, sys.stdin.readline().rstrip().split())
pokemon_master(n, m)
