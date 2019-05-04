import sys
from itertools import product

def main():
    input = sys.stdin.readline
    N = int(input())
    passwords = list(product(('a', 'b', 'c'), repeat=N))
    passwords = sorted(passwords)
    for p in passwords:
        print(''.join(p))

if __name__ == '__main__':
    main()
