import collections


def sleight_of_hand(k: int, array: str) -> int:
    counter = collections.Counter(array)
    answer = 0
    for j in range(1, 10):
        if counter[str(j)] <= 2 * k and counter[str(j)] != 0:
            answer += 1
    return answer


number = int(input())
arr = str()
for i in range(4):
    arr += input()
print(sleight_of_hand(number, arr))
