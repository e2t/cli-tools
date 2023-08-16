def main() -> None:
    words = {3: "Fizz", 5: "Buzz"}
    for i in range(1, 101):
        line = ""
        for num, word in words.items():
            if i % num == 0:
                line += word
        print(line if line else i)


if __name__ == "__main__":
    main()
