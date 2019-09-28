import sys

def main():
    input = sys.stdin.readline
    H, W, A, B = map(int, input().split())

    ans = []
    for h in range(B):
        row = [0]*A + [1]*(W-A)
        ans.append(row)
    
    for h in range(H-B):
        row = [1]*A + [0]*(W-A)
        ans.append(row)
    
    for a in ans:
        print(''.join(map(str, a)))

if __name__ == '__main__':
    main()