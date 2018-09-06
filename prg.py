import hashlib
import _md5
from datetime import datetime


def pseudo_random(seed,N):
    hash = str(seed).encode()
    k = 0;
    while k<N:
        now = datetime.now()
        hash = _md5.md5(hash * now.microsecond).digest()
        for c in hash:
            print(c/255)
            break;
        k=k+1;

if __name__ == '__main__':
    pseudo_random(0.2, 100);