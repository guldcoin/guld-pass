#! /usr/bin/env python3
__version__ = '0.0.1'
import argparse
from .index import get_pass, generate_pass

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
