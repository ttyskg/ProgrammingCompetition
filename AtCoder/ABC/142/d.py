import sys

def factorization(n):
    d = dict()
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            d[i] = cnt
    
    if temp != 1:
        d[temp] = 1
    
    if len(d) == 0:
        d[n] = 1
    
    return d

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if A == B == 1:
        return 1

    Af = factorization(A,)
    Bf = factorization(B,)
    cnt = 1
    for a in Af.keys():
        if a in Bf.keys():
            cnt += 1

    return cnt

if __name__ == '__main__':
    print(main())