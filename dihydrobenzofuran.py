#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

class dihydrobenzofuran:

    # op1: inverse
    # op2: xor
    # op3: bitshift right
    # op4: bitshift left
    # op5: substitute

    payload = b""

    def __init__(self, string):
        self.payload = bytes(string, "utf-8")

    # op1
    def inverse(self):
        self.payload = bytes(reversed(self.payload))

    # op2 xor
    def xor(self):
        for index in range(len(self.payload)):
            self.payload[index] = self.payload[index] ^ 0x4

    def bitshift_left(self):
        self.payload = self.payload << 0x23

    def bitshift_right(self):
        self.payload = self.payload >> 0x42

    def substitute(self):
        for i in range(len(self.payload)):
            if i % 2 is True:
                self.payload[i] = self.payload[i] & 0xFF

    def compute(self):
        self.inverse()
        self.xor()
        #self.bitshift_left()
        #self.bitshift_right()
        #self.substitute()

    def decrypt(self):
        self.compute()
        return self.payload

    def encrypt(self):
        self.compute()
        return self.payload


def main():
    string = "Hello ARM64"
    print("Original string: %s" %string)

    diescaline = dihydrobenzofuran(string)
    payload = diescaline.encrypt()

    print("dihydrobenzofuran encrypted:")
    print(payload)
    print("---")

    payload = diescaline.decrypt()

    print("dihydrobenzofuran decrypted:")
    print(payload)
    print("---")

if __name__ == "__main__":
    main()
