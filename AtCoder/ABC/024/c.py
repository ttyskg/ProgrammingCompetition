import sys

def main():
    input = sys.stdin.readline
    N, D, K = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(D)]
        
    for _ in range(K):
        s, t = map(int, input().split())
        if s < t:
            def pick(a):
                return max(a)
        else:
            def pick(a):
                return min(a)

        for i, (l, r) in enumerate(A, start=1):
            if l <= s <= r and l <= t <= r:
                print(i)
                break
            elif l <= s <= r:
                s = pick((l, r))


if __name__ == '__main__':
    main()
