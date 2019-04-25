import sys

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            y = self.find(self.root[x])
            self.root[x] = y
            return self.root[x]

    def unite(self, x, y):
        if self.is_same(x, y):
            return
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
            self.size[ry] += self.size[rx]
        else:
            self.root[ry] = rx
            self.size[rx] += self.size[ry]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    road = []
    for _ in range(M):
        a, b, y = map(int, input().split())
        road.append((y, a-1, b-1))

    road = sorted(road, key=lambda x: x[0])

    Q = int(input())
    question = []
    for i in range(Q):
        v, w = map(int, input().split())
        question.append((i, v-1, w))

    question = sorted(question, key=lambda x: -x[2])

    ans = [0 for _ in range(Q)]
    r = UnionFind(N)
    for i, v, w in question:
        while len(road) > 0 and road[-1][0] > w:
            _, a, b = road.pop()
            r.unite(a, b)

        ans[i] = r.size[r.find(v)]

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
