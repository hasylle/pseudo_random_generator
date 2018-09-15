import hashlib
import _md5
from datetime import datetime

def shift_lfsr(seed,mask_bits):
    lfsr = seed
    feedback = seed & 1
    while True:
        lfsr >>= 1
        if feedback == 1:
            lfsr ^= mask_bits
            break
        else:
            feedback = lfsr & 1
    return lfsr


def pseudo_random(seed,N):
    k = 0
    rand = []
    print(seed)
    shift_bits = seed % 5
    c = (seed ^ seed << shift_bits) & 0xFFFFFF
    print(c)
    a = (seed ^ c >> shift_bits) & 0xFFFFFF
    print(a)
    while k<N:
        # first algorithm -- linear congruential
        rand.append((a * seed + c))
        c = rand[k]
        #second algorithm -- LFSR
        lfsr = shift_lfsr(int(rand[k] * a), c)
        lfsr = shift_lfsr(lfsr,c)
        rand[k] = (lfsr & 0xffffff)
        #insert 2nd algorithm here

        #insert 3rd algorithm here

        #finally convert range to [0,1]
        rand[k] = rand[k] / 0xffffff
        k+=1
    if N == 1:
        return rand[0]
    return rand




if __name__ == '__main__':
    input = datetime.now().microsecond
    rand = pseudo_random(input, 10000)
    print(rand)