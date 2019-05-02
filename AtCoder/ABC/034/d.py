import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        w, p = map(int, input().split())
        salt = w * p / 100
        A.append((w, p, salt))

    A = sorted(A, key=lambda x: x[2])
    ans = A.pop()
    cnt = 1
    while cnt < K:
        w0 = ans[0]
        salt0 = ans[2]
        p = -1
        w = 0
        salt = 0
        pos = 0
        for i in range(len(A)):
            w1 = A[i][0]
            salt1 = A[i][2]

            p_ = (salt0 + salt1) / (w0 + w1) * 100
            if p_ > p:
                pos = i
                p = p_
                w = w0 + w1
                salt = salt0 + salt1

        ans = (w, p, salt)
        A.pop(pos)
        cnt += 1

    return ans[1]


if __name__ == '__main__':
    print(main())
