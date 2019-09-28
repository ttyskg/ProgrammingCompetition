import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N = int(input())
    e, o = 0, 0
    for i in range(1, N+1):
        if i % 2 == 0:
            e += 1
        else:
            o += 1

    return (o) / (e + o)

if __name__ == '__main__':
    print(main())