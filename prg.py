import hashlib
import _md5
from datetime import datetime


def shift_lfsr(seed, mask_bits):
    lfsr = seed
    feedback = seed & 1
    while True:
        lfsr >>= 1
        # print(feedback)
        if feedback == 1:
            lfsr ^= mask_bits
            break
        else:
            feedback = lfsr & 1
    return lfsr


def wilchman_hill(seed):
    a, x = divmod(seed, 30268)
    a, y = divmod(a, 30306)
    a, z = divmod(a, 30322)
    x = (171 * x) % 30269
    y = (172 * y) % 30307
    z = (170 * z) % 30323
    ret_val = (x / 30269.0 + y / 30307.0 + z / 30323.0) % 1.0
    print("Wilchman Hill: ", ret_val)
    return (x / 30269.0 + y / 30307.0 + z / 30323.0) % 1.0


def pseudo_random(seed, N):
    k = 0
    rand_list = []
    m1 = 30269
    m2 = 30307
    m3 = 30323
    print(seed)
    shift_bits = seed % 5
    print(shift_bits)
    x_n = (seed ^ seed << shift_bits) & 0xFFFFFF
    a = (seed ^ x_n >> shift_bits) & 0xFFFFFF
    print(a)
    while k < N:
        """
        First algorithm -- Wichman-Hill generator via linear congruential
        Formula for Wichman-Hill generator:
        rand = (x_n/m1 + y_n/m2 + z_n/m3) mod 1
        """
        random_number = wilchman_hill(seed)
        # random_number = (random_number ^ random_number << shift_bits) & 0xFFFFFF
        # random_number
        rand_list.append(random_number)
        random_number = rand_list[k]

        # Second algorithm -- LFSR
        # lfsr = shift_lfsr(int(rand_list[k] * a), random_number)
        # lfsr = shift_lfsr(lfsr, int(random_number))
        # rand_list[k] = (lfsr & 0xffffff)

        # Finally, convert range to [0,1]
        # rand_list[k] = rand_list[k] / 0xffffff
        k += 1
    if N == 1:
        return rand_list[0]
    return rand_list


if __name__ == '__main__':
    input = datetime.now().microsecond
    rand = pseudo_random(input, 10)
    print(rand)
