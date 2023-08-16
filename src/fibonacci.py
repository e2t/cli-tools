def main() -> None:
    a, b = 0, 1
    for _ in range(1, 21):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    main()
