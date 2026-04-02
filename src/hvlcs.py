import sys

def parse_input(text):
  
    lines = text.strip().splitlines()
    idx = 0

    k = int(lines[idx]); idx += 1
    values = {}
  
    for _ in range(k):
        parts = lines[idx].split(); idx += 1
        char, val = parts[0], int(parts[1])
        values[char] = val

    A = lines[idx].strip(); idx += 1
    B = lines[idx].strip(); idx += 1

    return values, A, B


def hvlcs(A, B, values):
  
    m, n = len(A), len(B)

    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    seq = []
    i, j = m, n
  
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            seq.append(A[i - 1])
            i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    seq.reverse()
    return dp[m][n], ''.join(seq)


def main():
  
    text = sys.stdin.read()
    values, A, B = parse_input(text)
    max_val, subseq = hvlcs(A, B, values)
    print(max_val)
    print(subseq)


if __name__ == '__main__':
    main()
