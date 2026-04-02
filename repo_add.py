import argparse

def main():

    parser = argparse.ArgumentParser(
        prog='pypac',
        description='Arch package manager, written in Python'
    )

    parser.add_argument("db_path")

    parser.add_argument("package_name")

    args: Namespace = parser.parse_args()

    print(args)


if __name__ == "__main__":
    main()
