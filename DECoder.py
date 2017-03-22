import base64
import html
import urllib.parse
import rsa
import pyDes


class Encoder:
    def base16(self, message=None):
        if message is not None:
            self.message = message

        self.encrypted = base64.b16encode(self.message.encode())

        return self.encrypted.decode()

    def base32(self, message=None):
        if message is not None:
            self.message = message

        self.encrypted = base64.b32encode(self.message.encode())

        return self.encrypted.decode()

    def base64(self, message=None):
        if message is not None:
            self.message = message

        self.encrypted = base64.b64encode(self.message.encode())

        return self.encrypted.decode()

    def caesar_cipher(self, message=None, shift=3):
        if message is not None:
            self.message = message

        for char in self.message:
            before = ord(char)
            before += shift
            after = chr(before)

            if self.encrypted is None:
                self.encrypted = after
            else:
                self.encrypted += after

        return self.encrypted

    def html(self, message=None):
        if message is not None:
            self.message = message

        self.encrypted = html.escape(self.message)

        return self.encrypted

    def url(self, message=None):
        if message is not None:
            self.message = message

        self.encrypted = urllib.parse.quote_plus(self.message)

        return self.encrypted

    def rsa(self, message=None, pub_key=None):
        if message is not None:
                self.message = message
        if pub_key is None:
            (pub_key, priv_key) = rsa.newkeys(256)
            generated = True
        else:
            generated = False

        self.encrypted = rsa.encrypt(self.message.encode(), pub_key)

        if generated:
            return [self.encrypted, pub_key, priv_key]
        return self.encrypted

    def des(self, message=None):


    def triple_des(self, message=None):

    def __init__(self, message=None):
        if message is None:
            self.message = None
        else:
            self.message = message
        self.encrypted = None


class Decoder:
    def base16(self, encrypted=None):
        if encrypted is not None:
            self.encrypted = encrypted

        self.message = base64.b16decode(self.encrypted.encode())

        return self.message.decode()

    def base32(self, encrypted=None):
        if encrypted is not None:
            self.encrypted = encrypted

        self.message = base64.b32decode(self.encrypted.encode())

        return self.message.decode()

    def base64(self, encrypted=None):
        if encrypted is not None:
            self.encrypted = encrypted

        self.message = base64.b64decode(self.encrypted.encode())

        return self.message.decode()

    def caesar_cipher(self, encrypted=None, shift=3):
        if encrypted is not None:
            self.encrypted = encrypted

        for char in self.encrypted:
            before = ord(char)
            before -= shift
            after = chr(before)
            if self.message is None:
                self.message = after
            else:
                self.message += after

        return self.message

    def html(self, encrypted=None):
        if encrypted is not None:
            self.encrypted = encrypted

        self.message = html.unescape(self.encrypted)

        return self.message

    def url(self, encrypted=None):
        if encrypted is not None:
            self.encrypted = encrypted

        self.message = urllib.parse.unquote_plus(self.encrypted)

        return self.message

    def rsa(self, priv_key, encrypted=None):
        if encrypted is not None:
            self.encrypted = encrypted

        self.message = rsa.decrypt(self.encrypted, priv_key)

        return self.message

    def __init__(self, encrypted=None):
        if encrypted is None:
            self.encrypted = None
        else:
            self.encrypted = encrypted
        self.message = None
