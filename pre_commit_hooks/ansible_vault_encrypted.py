"""
Finds unencrypted files, displays them and prevents the commit if found.
"""
import argparse


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        'extras', nargs='*',
        help='Extra file names to check',
    )
    args = parser.parse_args(argv)
    unencrypted_files = []
    for filename in args.filenames:
        check_me = False
        if '.vault.' in filename:
            check_me = True

        for extra in args.extras:
            if extra in filename:
                check_me = True
                break

        if not check_me:
            continue

        with open(filename, 'r') as f:
            first_line = f.readline()
            if 'ANSIBLE_VAULT' not in first_line:
                unencrypted_files.append(filename)
    if unencrypted_files:
        print('Found unencrypted files:\n')
        print("\n".join(unencrypted_files))
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
