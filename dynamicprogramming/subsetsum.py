def subset_exists(summation, array):
    num = len(array)
    matrix = [[0 for i in range(num)] for j in range(summation + 1)]

    for j in range(num):
        matrix[0][j] = 1
        if j == 0:
            matrix[array[0]][0] = 1
        else:
            for i in range(summation + 1):
                if matrix[i][j - 1] == 1:
                    matrix[i][j] = 1
                    if i + array[j] <= summation:
                        matrix[i + array[j]][j] = 1

    print(matrix)
    return matrix[summation][j]


def main():
    array = [int(i) for i in input().split()]
    array.sort()
    summation = int(input())
    print(subset_exists(summation, array))


if __name__ == '__main__':
    main()