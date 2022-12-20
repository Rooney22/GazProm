def psp(n: int, index: int,
        dif_branches: int, answer: list[str]):
    if dif_branches <= n-index-2:
        answer[index] = '('
        psp(n, index + 1, dif_branches + 1, answer)
    if dif_branches > 0:
        answer[index] = ')'
        psp(n, index + 1, dif_branches - 1, answer)
    if index == n:
        print(''.join(i for i in answer))


def main():
    n = int(input()) * 2
    answer = ['' for i in range(n)]
    psp(n, 0, 0, answer)


if __name__ == '__main__':
    main()