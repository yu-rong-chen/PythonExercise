import io

def main():
    long_description = read('README.rst')


def read(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()
