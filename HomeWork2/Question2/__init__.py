from functools import cmp_to_key


def comp(item1, item2):
    var1 = item1 + item2
    var2 = item2 + item1
    if var2 > var1:
        return 1
    if var2 < var1:
        return -1
    return 0


def largest_number(n: int, numbers: str) -> str:
    numbers = sorted(numbers.split(), key=cmp_to_key(comp))
    return ''.join(i for i in numbers)


def main():
    print(largest_number(int(input()), input()))


if __name__ == '__main__':
    main()
