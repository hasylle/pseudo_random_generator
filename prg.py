import hashlib
from datetime import datetime


def pseudo_random(seed,N):
    hash = str(seed).encode()
    k = 0;
    rand = [];
    while k<N:
        now = datetime.now()
        hash = hashlib.sha256(hash * now.microsecond).digest()
        for c in hash:
            rand.append(c/255)
            break;
        k=k+1;
    return rand
if __name__ == '__main__':
    rand = pseudo_random(0.2, 10);
    for a in rand:
        print(a)