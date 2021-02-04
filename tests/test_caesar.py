import unittest
from string import ascii_uppercase, ascii_lowercase, digits, punctuation, whitespace
from hiddenpower.commands.caesar import encrypt_content, decrypt_content


class CaesarTest(unittest.TestCase):
    # TODO test argument parsing

    def test_encrypt_rotation_uppercase_13(self):
        """test encrypt rotation uppercase -> k=13"""
        self.assertEqual(encrypt_content(ascii_uppercase), "NOPQRSTUVWXYZABCDEFGHIJKLM")

    def test_encrypt_rotation_lowercase_13(self):
        """test encrypt rotation lowercase -> k=13"""
        self.assertEqual(encrypt_content(ascii_lowercase), "nopqrstuvwxyzabcdefghijklm")

    def test_decrypt_rotation_uppercase_13(self):
        """test decrypt rotation uppercase -> k=13"""
        self.assertEqual(decrypt_content("NOPQRSTUVWXYZABCDEFGHIJKLM"), ascii_uppercase)

    def test_decrypt_rotation_lowercase_13(self):
        """test decrypt rotation lowercase -> k=13"""
        self.assertEqual(decrypt_content("nopqrstuvwxyzabcdefghijklm"), ascii_lowercase)

    def test_encrypt_non_ascii_letters_13(self):
        """test encrypt special chars like é, à, õ, ã, ç, etc... -> k=13"""
        content = punctuation + digits + whitespace + "àèáéíóúàãõâêîôûñ"
        self.assertEqual(encrypt_content(content), content)

    def test_decrypt_non_ascii_letters_13(self):
        """test decrypt special chars like é, à, õ, ã, ç, etc... -> k=13"""
        content = punctuation + digits + whitespace + "àèáéíóúàãõâêîôûñ"
        self.assertEqual(decrypt_content(content), content)

    def test_encrypt_key_gt_25(self):
        """test encrypt key > 25"""
        self.assertEqual(
            encrypt_content(ascii_uppercase, key=29), "DEFGHIJKLMNOPQRSTUVWXYZABC"
        )

    def test_decrypt_key_gt_25(self):
        """test decrypt key > 25"""
        self.assertEqual(
            decrypt_content("DEFGHIJKLMNOPQRSTUVWXYZABC", key=29), ascii_uppercase
        )

    def test_encrypt_key_lt_0(self):
        """test encrypt key < 25"""
        self.assertEqual(
            encrypt_content(ascii_lowercase, key=-3), "xyzabcdefghijklmnopqrstuvw"
        )

    def test_decrypt_key_lt_0(self):
        """test decrypt key < 25"""
        self.assertEqual(
            decrypt_content("xyzabcdefghijklmnopqrstuvw", key=-3), ascii_lowercase
        )
