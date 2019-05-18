import sys

def cross_check(A, B, C, D):
    ax, ay = A[0], A[1]
    bx, by = B[0], B[1]
    cx, cy = C[0], C[1]
    dx, dy = D[0], D[1]

    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

    return ta * tb < 0 and tc * td < 0


def main():
    input = sys.stdin.readline
    Ax, Ay, Bx, By = map(int, input().split())
    A = (Ax, Ay)
    B = (Bx, By)

    N = int(input())
    vertices = []
    for _ in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    # The first vertex is aslo used to define the last edge of the polygon.
    vertices.append((vertices[0]))

    cnt = 0
    for i in range(N):
        C = vertices[i]
        D = vertices[i+1]

        if cross_check(A, B, C, D):
            cnt += 1

    return 1 + cnt // 2


if __name__ == '__main__':
    print(main())
