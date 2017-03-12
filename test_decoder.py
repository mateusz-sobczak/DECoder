from unittest import TestCase
from DECoder import Decoder


class TestDecoder(TestCase):
    def setUp(self):
        self.decoder = Decoder()

    def test_caesar_cipher(self):
        self.assertEqual(self.decoder.caesar_cipher('khoor'), 'hello')

    def test_base64(self):
        self.assertEqual(self.decoder.base64('aGVsbG8='), 'hello')

    def test_base16(self):
        self.assertEqual(self.decoder.base16('68656C6C6F'), 'hello')

    def test_base32(self):
        self.assertEqual(self.decoder.base32('NBSWY3DP'), 'hello')

    def test_html(self):
        self.assertEqual(self.decoder.html('hello&gt;'), 'hello>')

    def test_url(self):
        self.assertEqual(self.decoder.url('hello%21'), 'hello!')
