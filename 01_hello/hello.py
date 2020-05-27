#!/usr/bin/env python3
# Purpose: say hello

import argparse

parser = argparse.ArgumentParser(description='Say Hello')
# parser.add_argument('name', help='Name to greet')
# make the argument optional
# note the keyword metavar used to describe what the value should be
parser.add_argument('-n', '--name', metavar='name',
                    default='World', help='Name to greet')
args = parser.parse_args()
# create a variable to capture the name namespace
name = args.name
print('Hello, ' + name + '!')
