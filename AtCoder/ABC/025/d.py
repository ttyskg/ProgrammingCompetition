import sys
from collections import defaultdict


def is_valid(state, pos):
    # Check if the position is filled; 0: empty, 1: filled, None: out of board.
    left  = state & (1 << (pos+1)) == 0 if pos % 5 != 4  else None
    right = state & (1 << (pos-1)) == 0 if pos % 5 != 0  else None
    up    = state & (1 << (pos+5)) == 0 if pos // 5 != 4 else None
    down  = state & (1 << (pos-5)) == 0 if pos // 5 != 0 else None

    if left != right and left is not None and right is not None:
        return False

    if up != down and up is not None and down is not None:
        return False

    return True


def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    A = []
    for _ in range(5):
        A += list(map(int, input().split()))

    reserved = dict()
    emp_pos = set(range(25))
    for i, a in enumerate(A):
        if a != 0:
            reserved[a] = i
            emp_pos.remove(i)

    dp = defaultdict(lambda: 0)
    dp[0] = 1
    for num in range(1, 26):
        dp_ = defaultdict(lambda: 0)
        
        # Prepare the positions where add new number to the board.
        # Note: the initially filled position can be excluded because only the
        # reserved number will fill in the position.
        positions = emp_pos
        if num in reserved:
            positions = [reserved[num]]

        for pos in positions:
            pb = 1 << pos  # Binary expression os pos
            for state, cnt in dp.items():
                # Check the position to add new number is empty.
                if state & pb > 0:
                    continue

                if is_valid(state, pos):
                    dp_[state | pb] += cnt

        # Update DP dict
        dp = dp_

    final_state = (1 << 25) - 1
    return dp[final_state] % MOD


if __name__ == '__main__':
    print(main())

