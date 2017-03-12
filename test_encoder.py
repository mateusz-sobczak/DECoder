from unittest import TestCase
from DECoder import Encoder


class TestEncoder(TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_base64(self):
        self.assertEqual(self.encoder.base64('hello'), 'aGVsbG8=')

    def test_caesar_cipher(self):
        self.assertEqual(self.encoder.caesar_cipher('hello'), 'khoor')

    def test_base32(self):
        self.assertEqual(self.encoder.base32('hello'), 'NBSWY3DP')

    def test_base16(self):
        self.assertEqual(self.encoder.base16('hello'), '68656C6C6F')

    def test_html(self):
        self.assertEqual(self.encoder.html('hello>'), 'hello&gt;')

    def test_url(self):
        self.assertEqual(self.encoder.url('hello!'), 'hello%21')
