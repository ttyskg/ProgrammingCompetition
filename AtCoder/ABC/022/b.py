import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cnt = 0
    visited = set()
    for _ in range(N):
        a = int(input())
        if a in visited:
            cnt += 1
        else:
            visited.add(a)

    return cnt


if __name__ == '__main__':
    print(main())
