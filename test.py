#!/usr/bin/env python3

def hello() -> int:
    return 999

if __name__ == "__main__":
    num = hello()
    if num > 200:
        print(num)
