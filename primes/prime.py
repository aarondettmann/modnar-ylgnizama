#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import os
from pathlib import Path


PROG_NAME = 'prime'

HERE = os.path.abspath(os.path.dirname(__file__))
FILE_LAST_PRIME = os.path.join(HERE, '.last_prime')

LAST_PRIME = 0


def gen_primes():
    """
    Infinite prime number generator using the Sieve of Eratosthenes

    Adapted from:
    * https://stackoverflow.com/questions/567222/simple-prime-generator-in-python

    Originally by:
    * David Eppstein, UC Irvine, 28 Feb 2002
    * http://code.activestate.com/recipes/117119/
    """

    # Maps composites (=non-primes) to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward" indefinitely,
    # but only as long as required by the current number being tested.
    D = {}

    q = 1  # the running integer that is checked for primeness
    while (q := q+1):
        if q not in D:
            # q is a new prime. Yield it and mark its first multiple that is
            # not already marked in previous iterations
            yield q
            D[q*q] = [q]
        else:
            # q is composite. D[q] is the list of primes that divide it. Since
            # we have reached q, we no longer need it in the map, but we will
            # mark the next multiples of its witnesses to prepare for larger
            # numbers
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]


def print_primes():
    global LAST_PRIME

    for p in gen_primes():
        if p <= LAST_PRIME:
            continue
        input(LAST_PRIME := p)


def cli():
    global LAST_PRIME

    parser = argparse.ArgumentParser(prog=f'{PROG_NAME}')
    parser.add_argument('--reset', '-r', action='store_true', help='reset count')
    args = parser.parse_args()

    if Path(FILE_LAST_PRIME).exists() and not args.reset:
        with open(FILE_LAST_PRIME, 'r') as fp:
            LAST_PRIME = int(fp.readline())

    try:
        print_primes()
    except KeyboardInterrupt:
        with open(FILE_LAST_PRIME, 'w') as fp:
            fp.write(str(LAST_PRIME))
        print("\nexit...", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    cli()
