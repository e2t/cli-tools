import os
import sys


def main() -> None:
    for i in sys.argv[1:]:
        filename = os.path.abspath(i)
        print(f"{filename}\nДлина {len(filename)} симв.\n")
    input()


if __name__ == "__main__":
    main()
