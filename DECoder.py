import base64


class Encoder:
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

    def __init__(self, message=None):
        if message is None:
            self.message = None
        else:
            self.message = message
        self.encrypted = None


class Decoder:
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

    def __init__(self, encrypted=None):
        if encrypted is None:
            self.encrypted = None
        else:
            self.encrypted = encrypted
        self.message = None
