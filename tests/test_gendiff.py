#!/usr/bin/python3


from gendiff.scripts.gendiff import generate_diff

def test_flat_json():
    assert generate_diff('file1.json file2.json') == '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''
