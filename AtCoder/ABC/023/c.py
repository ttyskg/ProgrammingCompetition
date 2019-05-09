import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    R, C, K = map(int, input().split())
    N = int(input())

    # Count points in each row and column.
    row_val = defaultdict(lambda: 0)
    col_val = defaultdict(lambda: 0)
    coordinate = []
    for _ in range(N):
        r, c = map(int, input().split())
        row_val[r] += 1
        col_val[c] += 1
        coordinate.append((r, c))

    # Count rows which have certain points.
    val_rows = defaultdict(lambda: 0)
    for _, v in row_val.items():
        val_rows[v] += 1

    # Count columns which have certain points.
    val_cols = defaultdict(lambda: 0)
    for _, v in col_val.items():
        val_cols[v] += 1

    ans = 0
    # Number of positions where the sum of row points ans column points is K.
    for v, n in val_rows.items():
        ans += n * val_cols[K-v]

    # Number of positions where the row/column point is K and the other is 0.
    ans += val_rows[K] * (C - len(col_val))
    ans += val_cols[K] * (R - len(row_val))

    # Dealing with the positions where the point is in.
    for r, c in coordinate:
        n = row_val[r]
        m = col_val[c]

        if n + m == K:
            ans -= 1
        
        if n + m == K+1:
            ans += 1

    return ans


if __name__ == '__main__':
    print(main())
