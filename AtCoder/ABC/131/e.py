import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    num = (N-1) * (N-2) // 2
    if K > num:
        print(-1)
        exit()

    edges = [(1, i) for i in range(2, N+1)]
    for j in range(2, N):
        for k in range(j+1, N+1):
            if num == K:
                break
            edges.append((j, k))
            num -= 1

    print(len(edges))
    for a, b in edges:
        print(a, b)


if __name__ == '__main__':
    main()
