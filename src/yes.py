import sys


def main() -> None:
    args = sys.argv[1:]
    line = ' '.join(args) if args else 'y'
    try:
        while True:
            print(line)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
