import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    if N <= 59:
        return 'Bad'
    elif N <= 89:
        return 'Good'
    elif N <= 99:
        return 'Great'
    else:
        return 'Perfect'

if __name__ == '__main__':
    print(main())
