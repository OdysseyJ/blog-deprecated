import copy

n = int(input())
lines = [input() for _ in range(n)]

arr = [["X" for _ in range(n)] for _ in range(n)]

for y, line in enumerate(lines):
    for x, a in enumerate(line):
        arr[y][x] = a

def check_difference(arr, p1, p2, n):
    x1, y1 = p1
    x2, y2 = p2
    if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
        return False
    if x1 >= n or x2 >= n or y1 >=  n or y2 >= n:
        return False
    if arr[y1][x1] == arr[y2][x2]:
        return False
    return True


def find_longest_seq(arr, n):
    max_sequence = 1

    # horizontal
    for y in range(n):
        max_line_seq = 1
        for x in range(n-1):
            if arr[y][x] == arr[y][x+1]:
                max_line_seq += 1
                if max_line_seq > max_sequence:
                    max_sequence = max_line_seq
            else:
                max_line_seq = 1

    # vertical
    for x in range(n):
        max_line_seq = 1
        for y in range(n-1):
            if arr[y][x] == arr[y+1][x]:
                max_line_seq += 1
                if max_line_seq > max_sequence:
                    max_sequence = max_line_seq
            else:
                max_line_seq = 1

    return max_sequence

total_max_sequence = 1
for y in range(n):
    for x in range(n):
        if check_difference(arr, (x, y), (x-1, y), n):
            arr_ = copy.deepcopy(arr)
            temp = arr_[y][x]
            arr_[y][x] = arr_[y][x-1]
            arr_[y][x-1] = temp
            max_seq = find_longest_seq(arr_, n)
            if max_seq > total_max_sequence:
                total_max_sequence = max_seq
        if check_difference(arr, (x, y), (x+1, y), n):
            arr_ = copy.deepcopy(arr)
            temp = arr_[y][x]
            arr_[y][x] = arr_[y][x+1]
            arr_[y][x+1] = temp
            max_seq = find_longest_seq(arr_, n)
            if max_seq > total_max_sequence:
                total_max_sequence = max_seq
        if check_difference(arr, (x, y), (x, y-1), n):
            arr_ = copy.deepcopy(arr)
            temp = arr_[y][x]
            arr_[y][x] = arr_[y-1][x]
            arr_[y-1][x] = temp
            max_seq = find_longest_seq(arr_, n)
            if max_seq > total_max_sequence:
                total_max_sequence = max_seq
        if check_difference(arr, (x, y), (x, y+1), n):
            arr_ = copy.deepcopy(arr)
            temp = arr_[y][x]
            arr_[y][x] = arr_[y+1][x]
            arr_[y+1][x] = temp
            max_seq = find_longest_seq(arr_, n)
            if max_seq > total_max_sequence:
                total_max_sequence = max_seq

print(total_max_sequence)
