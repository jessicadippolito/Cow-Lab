import sys
import heifer_generator

args = sys.argv
cows = heifer_generator.get_cows()


def list_cows(cows):
    for i in range(0,len(cows)-1):
        print(cows[i].name, end=' ')
    print(cows[len(cows)-1].name)


def find_cow(name, cows):
    for cow in cows:
        if cow.name == name:
            return cow

if args[1] == '-n':
    name = args[2]
    if (find_cow(name, cows)) == None:
        print(f'Could not find {name} cow!')
    else:
        for i in range(3,len(args)-1):
            print(args[i], end = ' ')
elif args[1] == '-l':
    print('Cows available: ', end = '')
    list_cows(cows)

