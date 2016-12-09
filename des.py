#!/usr/bin/env python
# -*- coding: utf8 -*-

# author: xiaofengfeng
# create: 2016-12-09 16:48:19


import pydes


if __name__ == '__main__':
    des = pydes.des('12345678', pydes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pydes.PAD_PKCS5)
    message = "qwertyuiopasdfghjklzxcvbnm"
    miwen = des.encrypt(message)
    print("encrypt: %r" % miwen)
    message = des.decrypt(miwen)
    print("decrypt: %r" % message)
