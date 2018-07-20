def longest_subsequence(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    matrix = [[0 for x in range(m)] for y in range(n)]

    for j in range(1, m):
        for i in range (1, n):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j - 1])

    return matrix[n - 1][m - 1]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(longest_subsequence(str1, str2))