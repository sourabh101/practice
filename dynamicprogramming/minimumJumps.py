def get_minimum_jumps(array):
    length = len(array)
    result = [0 for i in range(length)]
    for j in range(1, length):
        for i in range(0, j):
            if j <= i + array[i]:
                if result[j] == 0:
                    result[j] = result[i] + 1
                else:
                    result[j] = min(result[i] + 1, result[j])

    return result[length - 1]


def main():
    array = [int(i) for i in input().split()]
    print(get_minimum_jumps(array))


if __name__ == '__main__':
    main()
