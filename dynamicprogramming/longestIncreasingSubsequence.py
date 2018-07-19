def longest_sub_sequence(num_list):
    num = len(num_list)
    res = []
    for i in range(0, num):
        res.append(1)

    for j in range(1, num):
        for i in range(0, j):
            if num_list[j] > num_list[i]:
                if res[i]== res[j]:
                    res[j] = res[i] + 1

    return max(res)


if __name__ == '__main__':
    num_list = [int(str) for str in input().split()]
    print(longest_sub_sequence(num_list))