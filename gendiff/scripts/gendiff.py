#!/usr/bin/python3


import argparse
import json


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('-f', '--format', help='set format of output')
parser.add_argument('first_file')
parser.add_argument('second_file')

args = parser.parse_args()

def main():
    with open(args.first_file) as handle:
        file1 = json.loads(handle.read())
    with open(args.second_file) as handle:
        file2 = json.loads(handle.read())
    print('\nstart\n')
    print(file1, file2)



