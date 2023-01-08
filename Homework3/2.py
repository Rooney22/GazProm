import re


def is_palindrome(sentence: str) -> bool:
    sentence = re.sub('\W+', '', sentence).lower()
    return sentence == sentence[::-1]


def main():
    print(is_palindrome(input()))


if __name__ == '__main__':
    main()
