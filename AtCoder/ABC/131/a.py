import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())

    a = ''
    for s in S:
        if s == a:
            return 'Bad'
        a = s

    return 'Good'


if __name__ == '__main__':
    print(main())
