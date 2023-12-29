#!/usr/bin/python3
import sys


def get_prime(files):
    if not isinstance(files, str):
        sys.exit(1)
    with open(files, "r") as file:
        for line in file:
            n = int(line)
            div_sor = 2
            prime_no = []
            while n > 1:
                if n % div_sor == 0:
                    prime_no.append(div_sor)
                    prime_no.append(int(n // div_sor))
                    break
                else:
                    div_sor += 1
            print("{:d}={}*{}".format(n, prime_no[0], prime_no[1]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage ./{} filename".format(sys.argv[0]))
    else:
        files = sys.argv[1]
    get_prime(files)
