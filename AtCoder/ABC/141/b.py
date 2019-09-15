import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())

    for i, s in enumerate(S, start=1):
        if i%2 == 1:
            if s not in ('R', 'U', 'D'):
                return 'No'
        else:
            if s not in ('L', 'U', 'D'):
                return 'No'

    return 'Yes'


if __name__ == '__main__':
    print(main())
