import sys

def calc_points(B, C, board):
    s, t = 0, 0
    for i in range(9):
        x = board[i]
        if x == '0':
            continue

        # The position of x on the 3x3 board.
        r = i // 3
        c = i % 3

        # Score calculation based on condition B.
        if i <= 5:
            y = board[i+3]  # The mark located under x.

            if x == y:
                s += B[r][c]
            elif y != '0':
                t += B[r][c]

        # Score calculation based on condition C.
        if i % 3 < 2:
            z = board[i+1]  # The mark located to the right of x.

            if x == z:
                s += C[r][c]
            elif z != '0':
                t += C[r][c]

    return (s, t, s-t)


def get_next(board, t):
    # The player is Chokudai when t is odd, and the player is Naoko when t is even.
    if t % 2 == 1:
        mark = '1'
    else:
        mark = '2'

    res = []
    for i, m in enumerate(board):
        if m != '0':
            continue

        b = board[:i] + mark + board[i+1:]
        res.append(b)

    return res


def minmax(scores, t):
    if t % 2 == 1:  # Turn of Chokudai. Chokudai tries to maximize the score
        score = -float('inf')
        def pick(a, b):
            return max(a, b)

    else:  # Turn of Naoko. Naoko tries to minimize the score.
        score = float('inf')
        def pick(a, b):
            return min(a, b)

    for s in scores:
        score = pick(score, s)

    return score


def dfs(B, C, board, memo=dict(), t=0):
    if t == 9:
        return calc_points(B, C, board)

    if board in memo:
        return memo[board]

    next_b = get_next(board, t+1)
    points = []
    scores = []
    for nb in next_b:
        point = dfs(B, C, nb, memo, t+1)
        points.append(point)
        scores.append(point[2])

    score = minmax(scores, t+1)
    for p in points:
        if p[2] == score:
            memo[board] = p
            return p


def main():
    input = sys.stdin.readline
    B = [list(map(int, input().split())) for _ in range(2)]
    C = [list(map(int, input().split())) for _ in range(3)]

    board = '0' * 9  # condition of the board. 1: circle, 2: cross, 0: empty.
    p = dfs(B, C, board)
    print(p[0])
    print(p[1])


if __name__ == '__main__':
    main()
