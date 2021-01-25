#!/usr/bin/python3

import sys
from caesar import encrypt,decrypt

def main():
    cipher_type = sys.argv[1]
    argument = sys.argv[2]
    content = sys.argv[3]

    opt = {
        'caesar': {
            '-d': decrypt,
            '-e': encrypt
        }
    }

    try:
        r = opt[cipher_type][argument](content)
        print(r)
    except KeyError:
        print("Invalid command\n")

   
if __name__ == '__main__':
	main()