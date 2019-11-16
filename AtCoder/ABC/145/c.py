import sys
from itertools import permutations

def main():
    input = sys.stdin.readline
    N = int(input())
    pos = []
    for _ in range(N):
        x, y = map(int, input().split())
        pos.append((x, y))
    
    dists = []
    for root in permutations(range(N), N):
        d = 0
        for i in range(N-1):
            a = root[i]
            b = root[i+1]
            Xd = pos[a][0] - pos[b][0]
            Yd = pos[a][1] - pos[b][1]

            d += (Xd**2 + Yd**2)**0.5
        
        dists.append(d)
    
    return sum(dists) / len(dists)

if __name__ == '__main__':
    print(main())