from string import ascii_lowercase,ascii_uppercase


ALPHABET = {
    "lowercase": ascii_lowercase,
    "uppercase": ascii_uppercase
}
key = 13

def cipher(content, direction, key):
    result = ''

    for char in content:
        if char in ALPHABET["lowercase"]:
            index = ALPHABET["lowercase"].index(char)
            result += ALPHABET["lowercase"][(index + direction * key) % len(ALPHABET["lowercase"])]
        elif char in ALPHABET["uppercase"]:
            index = ALPHABET["uppercase"].index(char)
            result += ALPHABET["uppercase"][(index + direction * key) % len(ALPHABET["uppercase"])]
        else:
            result += char

    return result


def encrypt(content, key=key):
    return cipher(content, 1, key)


def decrypt(content, key=key):
    return cipher(content, -1, key)


def help():
    print("""
    -d decrypt
    -e encrypt
    -h help
    """)
    pass