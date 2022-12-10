def nearest_zero(len_array: int, array: list[int]) -> str:
    answer = []
    distance = 0
    first = True
    i = 0
    while i < len_array:
        answer.append(distance)
        if array[i] == 0 and first:
            first = False
            for x in range(i, -1, -1):
                answer[x] = i-x
            distance = 0
        elif array[i] == 0:
            answer[i] = 0
            for x in range(i, i - int(distance / 2) - 1, -1):
                answer[x] = i - x
            distance = 0
        i += 1
        distance += 1
    return str(answer)


arr = list(map(int, input().split()))
print(nearest_zero(len(arr), arr))
