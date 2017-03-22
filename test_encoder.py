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

    def test_rsa(self):
        import rsa
        publicKey = rsa.PublicKey(68706731939835159529538476419799965655742346573230197443885147162104769051533, 65537)
        self.assertNotEqual(self.encoder.rsa('hello', publicKey),
                            '\x94\x06=\xed\xfa\x9c\xa6\x8a,\xa6\xb3H\xb6T\xec\x04\x89gm\xc1:\xc5"\\-\xb5 %g\x08^}'.encode())

    def test_des(self):
        self.assertEquals(self.encoder.des(message='hello'), b'\x10\xf5\x99%\x02H\xdd\x1e')
