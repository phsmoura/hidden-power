from string import ascii_lowercase, ascii_uppercase
import click


ALPHABET = {"lowercase": ascii_lowercase, "uppercase": ascii_uppercase}
DEFAULT_KEY = 13


def cipher(content, direction, key):
    result = ""

    for char in content:
        if char in ALPHABET["lowercase"]:
            index = ALPHABET["lowercase"].index(char)
            result += ALPHABET["lowercase"][
                (index + direction * key) % len(ALPHABET["lowercase"])
            ]
        elif char in ALPHABET["uppercase"]:
            index = ALPHABET["uppercase"].index(char)
            result += ALPHABET["uppercase"][
                (index + direction * key) % len(ALPHABET["uppercase"])
            ]
        else:
            result += char

    return result


def encrypt_content(content, key=DEFAULT_KEY):
    return cipher(content, 1, key)


def decrypt_content(content, key=DEFAULT_KEY):
    return cipher(content, -1, key)


@click.command()
@click.option(
    "--encrypt/--decrypt",
    "-e/-d",
    required=True,
    default=False,
    help="Encrypt/Decrypt content",
)
@click.argument("file", type=click.Path(exists=False))
@click.option(
    "-k", "--key", required=False, default=DEFAULT_KEY, help="Define key, default is 13"
)
def cli(encrypt, file, key):
    """Encrypt or decrypt content with caesar's cypher"""

    content = ""
    with open(file) as f:
        content += f.read()

    if encrypt:
        print(encrypt_content(content, key=key))
    else:
        print(decrypt_content(content, key=key))
