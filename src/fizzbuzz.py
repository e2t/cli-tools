def main() -> None:
    words = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, 101):
        is_multi_any = False
        for num, word in words.items():
            if i % num == 0:
                is_multi_any = True
                print(word, end='')
        if not is_multi_any:
            print(i)
        else:
            print()


if __name__ == '__main__':
    main()
