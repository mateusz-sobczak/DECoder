from unittest import TestCase
from DECoder import Decoder


class TestDecoder(TestCase):
    def setUp(self):
        self.decoder = Decoder()

    def test_caesar_cipher(self):
        self.assertEqual(self.decoder.caesar_cipher('khoor'), 'hello')

    def test_base64(self):
        self.assertEqual(self.decoder.base64('aGVsbG8='), 'hello')
