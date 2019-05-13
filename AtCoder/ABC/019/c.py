import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    res = set()
    for a in A:
        while a % 2 == 0:
            a //= 2

        res.add(a)
            
    return len(res)


if __name__ == '__main__':
    print(main())
