def bin_number(number: int) -> str:
    answer = ""
    minus = ""
    if number < 0:
        minus = "-"
        number *= -1
    elif number == 0:
        return "0"
    while number > 0:
        answer += str(number % 2)
        number //= 2

    return minus + answer[::-1]


def main():
    print(bin_number(int(input())))


if __name__ == '__main__':
    main()
