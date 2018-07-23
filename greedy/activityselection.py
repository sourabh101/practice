def get_max_activities(list_start, list_end):
    count = 0
    prev_end = 0
    for i in range(len(list_end)):
        if count == 0:
            count += 1
            prev_end = list_end[i]
        else:
            if list_start[i] >= prev_end:
                count += 1
                prev_end = list_end[i]
    return count


def main():
    num = int(input())
    list_start = [int(i) for i in input().split()]
    # end time should be sorted
    list_end = [int(i) for i in input().split()]
    print(get_max_activities(list_start, list_end))
if __name__ == '__main__':
    main()

