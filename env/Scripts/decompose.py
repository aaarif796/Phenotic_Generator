#!F:\MCA\2nd Sem\Object Oriented Programming (OOP)\Phonetic Translation\phonetic\env\Scripts\python.exe

import unicodedata
import sys


def main(fn):
    with open(fn, encoding='utf-8') as f:
        print(unicodedata.normalize('NFD', f.read()))


if __name__ == '__main__':
    main(sys.argv[1])
