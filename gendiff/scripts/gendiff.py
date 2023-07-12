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
    
    result = '{\n'

    for i in sorted(file1.keys()|file2.keys()):
        if i in file1.keys():
            if i in file2.keys():
                if file1[i] == file2[i]:
                    result = result + '   ' + i + ': ' + str(file1[i]) + '\n'
                else:
                    result = result + ' - ' + i + ': ' + str(file1[i]) + '\n'
                    result = result + ' + ' + i + ': ' + str(file2[i]) + '\n'
            else:
                result = result + ' - ' + i + ': ' + str(file1[i]) + '\n'
        else:
            result = result + ' + ' + i + ': ' + str(file2[i]) + '\n'
    result = result + '}'

    return result



