#!/usr/bin/env python3
import sys

def rot13(text):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rot   = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    table = str.maketrans(alpha, rot)
    return text.translate(table)

if __name__ == "__main__":
    # If arguments exist, join them; otherwise read from pipe/stdin
    data = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read()
    print(rot13(data).strip())