def get_max_value(weights, values, max_weight):
    n = max_weight + 1
    m = len(weights)
    matrix = [[0 for i in range(m)] for j in range(n)]

    for j in range(m):
        for i in range(n):
            if i < weights[j]:
                if i > 0:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = 0
            else:
                if j > 0:
                    matrix[i][j] = max(matrix[i][j - 1], values[j] + matrix[i - weights[j]][j-1])
                else:
                    matrix[i][j] = values[j] + matrix[i - weights[j]][j-1]

    return matrix[n-1][m-1]


def main():
    # weights should be sorted in increasing order
    weights = [int(i) for i in input().split()]
    values = [int(i) for i in input().split()]
    max_weight = int(input())
    print(get_max_value(weights, values, max_weight))


if __name__ == '__main__':
    main()

