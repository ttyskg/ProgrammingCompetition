import sys

def main():
    input = sys.stdin.readline
    a = int(input())
    b = int(input())

    return (b - a%b) % b


if __name__ == '__main__':
    print(main())
