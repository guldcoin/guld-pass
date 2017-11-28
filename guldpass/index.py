#! /usr/bin/env python3
import os
from random import randint
from subprocess import check_output

try:
    GEN_PASS_LEN = os.environ['GEN_PASS_LEN']
except KeyError:
    # is this pseudo-randomized length actually helping?
    GEN_PASS_LEN = 25 + randint(-5, 5)

def get_pass(account):
    return check_output("pass " + account, shell=True).splitlines()[0]

def generate_pass(account):
    return check_output("pass generate %s %s" % (account, GEN_PASS_LEN), shell=True).splitlines()[-1]

