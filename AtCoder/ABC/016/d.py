import sys

def get_linear_formula(x0, y0, x1, y1):
    # Return the slope and intercept of the line passing (x0, y0) and (x1, y1). 
    if x0 == x1:  # The linear is parallel to x-axis.
        slope = None
    else:
        slope = (y1 - y0) / (x1 - x0)

    if slope is None:
        intercept = x0  # x = intercept.
    else:
        intercept = y0 - slope * x0  # y = slope * x + intercept.

    return slope, intercept


def get_intersection(slope0, intercept0, slope1, intercept1):
    if slope0 is None:
        return intercept0, slope1 * intercept0 + intercept1

    if slope1 is None:
        return intercept1, slope0 * intercept1 + intercept0

    cross_x = (intercept0 - intercept1) / (slope1 - slope0)
    cross_y = slope0 * cross_x + intercept0

    return cross_x, cross_y


def main():
    input = sys.stdin.readline
    Ax, Ay, Bx, By = map(int, input().split())

    # Get the slope and intercept of the KARATE-chop.
    slope_ab, intercept_ab = get_linear_formula(Ax, Ay, Bx, By)

    N = int(input())
    vertices = []
    for _ in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    # The first vertex is aslo used to define the last edge of the polygon.
    vertices.append((vertices[0]))

    x0, y0 = vertices[0]
    cnt = 0
    for x1, y1 in vertices[1:]:
        slope, intercept = get_linear_formula(x0, y0, x1, y1)

        if slope == slope_ab:  # The KARATE-chop and the edge is parallel.
            x0 = x1
            y0 = y1
            continue

        xc, yc = get_intersection(slope, intercept, slope_ab, intercept_ab)

        # Check the intersection is on the KARATE-chop and the edge.
        on_KC = min(Ax, Bx) <= xc <= max(Ax, Bx) and\
                min(Ay, By) <= yc <= max(Ay, By)
        on_edge = min(x0, x1) <= xc <= max(x0, x1) and\
                  min(y0, y1) <= yc <= max(y0, y1)

        if on_KC and on_edge:
            cnt += 1

        x0 = x1
        y0 = y1

    return 1 + cnt // 2


if __name__ == '__main__':
    print(main())
