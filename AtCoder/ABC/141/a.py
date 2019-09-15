import sys

def main():
    input = sys.stdin.readline
    S = str(input().strip())

    d = {'Sunny': 'Cloudy',
         'Cloudy': 'Rainy',
         'Rainy': 'Sunny'}

    return d[S]


if __name__ == '__main__':
    print(main())
