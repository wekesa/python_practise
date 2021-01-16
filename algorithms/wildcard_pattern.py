
def string_match(strr, pattern):
    n = len(strr)
    m = len(pattern)

    if m == 0:
        return n == 0

    lookup = [[False for i in range(m+1)] for j in range(n+1)]

    # empty pattern can match with empty string
    lookup[0][0] = True

    for k in range(1, m+1):
        if (pattern[k-1] == '*'):
            lookup[0][k] = lookup[0][k-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[i][j] == '*':
                lookup[i][j] = lookup[i][j] or lookup[i-1][j-1]

            elif pattern[j-1] == '?' or strr[i-1]==pattern[j-1]:
                lookup[i][j] = lookup[i-1][j-1]
            else:
                lookup[i][j] = False
    return lookup[n][m]


if __name__ == '__main__':
    strr = "baaabab"
    pattern = "*****ba*****ab"
    print(string_match(strr, pattern))