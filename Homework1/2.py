def sleight_of_hand(k: int, array: str) -> int:
    answer = sum(0 < array.count(str(i)) <= 2 * k for i in range(0, 10))
    return answer


def main():
    number = int(input())
    arr = ''.join((input()) for i in range(4))
    print(sleight_of_hand(number, arr))


if __name__ == '__main__':
    main()
