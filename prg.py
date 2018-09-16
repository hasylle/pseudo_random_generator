import hashlib
import _md5
from datetime import datetime

def shift_lfsr(seed):
    """
    Galois LFSR Implementaion
    Feedback polynomial used: polynomial: x^16 + x^14 + x^13 + x^11 + 1
    Equivalent polynomial mask: 0xB400
    This polynomial mask makes sure output ranges until 65535
    :param seed:
    :return: generated lfsr
    """
    lfsr = seed
    feedback = seed & 1
    lfsr >>= 1
    if feedback == 1:
        lfsr ^= 0xB400
    return lfsr

def wichmann_hill(seed):
    """
    Wichmann-Hill generator via linear congruential
    Formula for Wichmann-Hill generator:
    rand = (x_n/m1 + y_n/m2 + z_n/m3) mod 1
    :param seed:
    :return: ret_val: random number generated
    """
    a, x = divmod(seed, 30268)
    a, y = divmod(a, 30306)
    a, z = divmod(a, 30322)
    x = (171 * x) % 30269
    y = (172 * y) % 30307
    z = (170 * z) % 30323
    ret_val = (x / 30269.0 + y / 30307.0 + z / 30323.0) % 1.0
    return ret_val

def pseudo_random(seed,N):
    k = 0
    rand = []
    lfsr = seed
    while k<N:
        """
        First algorithm -- Linear Feedback Shift Register Algorithm
        """
        lfsr = shift_lfsr(lfsr)
        lfsr = shift_lfsr(lfsr) #shift twice to increase randomness
        rand.append(lfsr)
        """
        Second algorithm -- Wichman-Hill generator via linear congruential
        """
        rand[k] = wichmann_hill(rand[k])
        k+=1
    if N == 1:
        return rand[0]
    return rand

if __name__ == '__main__':
    input = datetime.now().microsecond
    rand = pseudo_random(input, 10000)
    print(rand)
