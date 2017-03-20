import base64
import html
import urllib.parse
import rsa


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
            exit(0)
            # TODO add generating public keys

        self.encrypted = rsa.encrypt(self.message, pub_key)

        # TODO need to write a test
        return [pub_key, self.encrypted]

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

    def rsa(self, encrypted=None, priv_key=None):
        if encrypted is not None:
            self.encrypted = encrypted
        if priv_key is None:
            exit(0)
            # TODO add generating private keys

        self.message = rsa.decrypt(self.encrypted, priv_key)

        # TODO need to write a test
        return self.message

    def __init__(self, encrypted=None):
        if encrypted is None:
            self.encrypted = None
        else:
            self.encrypted = encrypted
        self.message = None
