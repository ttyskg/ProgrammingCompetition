import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())
    K = int(input())

    ans = 0
    if len(S) == 1:
        return K // 2
    
    if len(set(S)) == 1:
        return len(S) * K // 2
    
    l, r = 0, 0
    if S[0] == S[-1]:
        while len(set(S[0:l+1])) <= 1:
            l += 1
        while len(set(S[-r-1:])) <= 1:
            r += 1
    
    cnt = 0
    T = S[0]
    for s in S[1:]:
        if s == T[-1]:
            cnt += 1
            T += '_'
        else:
            T += s
    
    ans = cnt * K
    if max(l, r) >= 1:
        ans -= (l//2 + r//2 - (l+r)//2) * (K-1)
    
    return ans

if __name__ == '__main__':
    print(main())