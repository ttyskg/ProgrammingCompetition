import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    N2 = bin(N)[2:][::-1]

    ans = []
    for i, c in enumerate(N2):
        if c != '0':
            ans.append(2**i)

    print(len(ans))
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
