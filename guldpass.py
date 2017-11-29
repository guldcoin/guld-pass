#! /usr/bin/env python3
__version__ = '0.0.1'
import os
import argparse
from random import randint
from subprocess import check_output
#from .index import get_pass, generate_pass

try:
    GEN_PASS_LEN = os.environ['GEN_PASS_LEN']
except KeyError:
    # is this pseudo-randomized length actually helping?
    GEN_PASS_LEN = 25 + randint(-5, 5)

def get_pass(account):
    return check_output("pass " + account, shell=True).splitlines()[0]

def generate_pass(account):
    return check_output("pass generate %s %s" % (account, GEN_PASS_LEN), shell=True).splitlines()[-1]

def main():
    parser = argparse.ArgumentParser('guld-pass')
    parser.add_argument("command", type=str, default="get", choices=["get", "generate"])
    parser.add_argument("account", type=str, help="The account to run command on.")
    args = parser.parse_args()
    if args.command == 'get':
        print(get_pass(args.account))
    elif args.command == 'generate':
        print(generate_pass(args.account))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

