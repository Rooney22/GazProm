def bin_number(number: int) -> str:
    answer = ""
    while number > 0:
        answer += str(number % 2)
        number //= 2

    return answer[::-1]


def main():
    print(bin_number(int(input())))


if __name__ == '__main__':
    main()
