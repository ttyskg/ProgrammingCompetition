import sys

def main():
    input = sys.stdin.readline
    N = int(input())

    N2 = bin(N)[2:]
    if len(N2) % 2 == 0:
        opt2 = '10' * (len(N2) // 2)
        opt10 = int(opt2, 2)

        if opt10 <= N:
            return 'Aoki'
        else:
            return 'Takahashi'

    else:
        opt2 = '1' + '01' * (len(N2) // 2)
        opt10 = int(opt2, 2)

        if opt10 <= N:
            return 'Takahashi'
        else:
            return 'Aoki'


if __name__ == '__main__':
    print(main())
