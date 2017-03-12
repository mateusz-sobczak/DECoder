from unittest import TestCase
from DECoder import Encoder


class TestEncoder(TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_base64(self):
        self.assertEqual(self.encoder.base64('hello'), 'aGVsbG8=')

    def test_caesar_cipher(self):
        self.assertEqual(self.encoder.caesar_cipher('hello'), 'khoor')

