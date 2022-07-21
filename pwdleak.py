#!/usr/bin/env python3

from requests import get
from hashlib import sha1

def searchPublicPasswords(p:str) -> int:
    p= sha1(p.encode()).hexdigest().upper()
    hash_list = get(f"https://api.pwnedpasswords.com/range/{p[:5]}")
    hash_list = hash_list.text.splitlines()
    
    for hash in hash_list:
        if p[5:] == hash[:35]:
            return int(hash[36:])
    return 0

if __name__ == '__main__':

    import sys

    if len(sys.argv) <= 1:
        print('\x1b[1;30;44m Note: \x1b[0m'+ " Give passwords as parameters.")
        sys.exit()
    elif sys.argv[1] == '-f':
        with open(sys.argv[2],'r') as f:
            args = f.read().splitlines()
    else:
        args = sys.argv[1:]

    print("-"*40)
    for arg in args:
        count = searchPublicPasswords(arg)
        if count > 0:
            print(f"\x1b[0;30;41m\t{arg}\x1b[0m  [{count}]")
        else:
            print(f"\x1b[0;30;42m\t{arg}\x1b[0m  [{count}]")

        print("-"*40)