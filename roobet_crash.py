
# import matplotlib.pyplot as plt
# import numpy as np
import hashlib
import random
import string
import hmac

salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
game_hash = '100af1b49f5e9f87efc81f838bf9b1f5e38293e5b4cf6d0b366c004e0a8d9987'

def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0

print(get_result(game_hash))

