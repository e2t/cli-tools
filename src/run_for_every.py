import os
import subprocess
from argparse import ArgumentParser

# --wait --cmd "...\solidworksexplorer.exe" rename -- %P%S


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('--wait', action='store_true')
    parser.add_argument('--cmd', required=True, nargs='+')
    parser.add_argument('filename', nargs='+')
    args = parser.parse_args()

    cmd = args.cmd + [None]
    size = len(args.filename)
    for i, f in enumerate(args.filename):
        print(f'{round((i + 1) / size * 100):2d}% - {os.path.basename(f)}')
        cmd[-1] = f
        if args.wait:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.Popen(cmd, shell=True)


if __name__ == '__main__':
    main()
