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

    def test_rsa(self):
        import rsa
        privateKey = rsa.PrivateKey(68706731939835159529538476419799965655742346573230197443885147162104769051533,
                                    65537,
                                    19061382122008680143523026355567129629292323946827194069036011864529823625833,
                                    57075922549895275552549577057264864809031, 1203777860616660755154882879116047243)
        message = b'\x80\xbc\xc9\xca?\xf9\xd7\x82YNC\x1a\xb0\xde\xee\xb9\x89\x94\xa7\xf5\xcc\xbb\xde\xd9gc\xfd\x83S\x11wX'

        self.assertEqual(self.decoder.rsa(privateKey, message), 'hello'.encode())

    def test_des(self):
        self.assertEquals(self.decoder.des(encrypted=b'\x10\xf5\x99%\x02H\xdd\x1e'), b'hello')
