#!/usr/bin/python3


from gendiff.scripts.gendiff import generate_diff


file1 = 'tests/file1.json'
file2 = 'tests/file2.json'

def test_flat_json():
    diff = generate_diff(file1, file2)
    assert diff == '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''
