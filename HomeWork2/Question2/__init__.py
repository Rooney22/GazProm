def largest_number(n: int, numbers: str) -> str:
    numbers = numbers.split()
    for i in range(n - 1):
        for j in range(n - i - 1):
            var1 = numbers[j] + numbers[j+1]
            var2 = numbers[j+1] + numbers[j]
            if var2 > var1:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return ''.join(i for i in numbers)


def main():
    print(largest_number(int(input()), input()))


if __name__ == '__main__':
    main()