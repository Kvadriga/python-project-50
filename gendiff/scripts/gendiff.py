#!/usr/bin/python3


import argparse
import json
import yaml


def generate_diff(file_path1, file_path2):
    with open(file_path1) as handle, open(file_path2) as handle2:
        if file_path1[-4:] == 'json':
            file1 = json.loads(handle.read())
            file2 = json.loads(handle2.read())
        if file_path1[-4:] == 'yaml' or file_path1[-3:] == 'yml':
            file1 = yaml.safe_load(handle.read())
            file2 = yaml.safe_load(handle2.read())

    result = '{\n'

    for i in sorted(file1.keys() | file2.keys()):
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


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration '
                                                 'files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)


if __name__ == '__main__':
    main()
