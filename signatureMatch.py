#!/usr/bin/env python

import sys, os, binascii
from argparse import ArgumentParser
from base64 import b16encode


def check_sig(fn):
    ''' Hex dump the file and search for signatures '''

    with open(fn, 'rb') as f:
        #file_sig_hex = binascii.hexlify(f.read(4))
        file_sig_hex = b16encode(f.read(4)).decode('utf-8')
        return file_sig_hex


# Main
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", help="Detect signatures in file at this path")

    args = parser.parse_args()

    results = check_sig(args.file_path)
    print(results)

