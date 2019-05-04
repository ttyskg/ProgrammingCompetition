import sys

def get_move(R):
    c = set()
    for r in R:
        if len(r) < 1:
            return None
        c.add(r[0])

    if len(c) >= 3:
        return None

    elif len(c) == 1:
        if 'R' in c:
            return 'P'
        elif 'P' in c:
            return 'S'
        else:
            return 'R'

    else:
        if c == set(('R', 'P')):
            return 'P'
        elif c == set(('P', 'S')):
            return 'S'
        else:
            return 'R'


def eliminate_losers(R, mv):
    lose = {'R': 'S', 'S': 'P', 'P': 'R'}
    l = lose[mv]

    res = []
    for r in R:
        if r[0] == l:
            continue
        res.append(r[1:])

    return res


def main():
    input = sys.stdin.readline
    T = int(input())
    for t in range(1, T+1):
        A = int(input())
        robots = []
        for _ in range(A):
            p = str(input().strip())
            num = len(p)
            p = p * (500 // num) + p[:500%num]
            
            robots.append(p)

        ans = ''
        while len(robots) > 0:
            mv = get_move(robots)
            if mv is None:
                ans = 'IMPOSSIBLE'
                break

            ans += mv
            robots = eliminate_losers(robots, mv)

        print('Case #{}: {}'.format(t, ans))


if __name__ == '__main__':
    main()
