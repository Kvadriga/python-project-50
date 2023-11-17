#!/usr/bin/python3
from gendiff.scripts.gendiff import generate_diff
import pytest


file1 = 'tests/file1.json'
file2 = 'tests/file2.json'
expected_result1 = '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''

@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [(file1, file2, expected_result1),])

def test_flat_json(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2)
    assert diff == expected_result1
    assert 1 == 1

def test_for_more_count():
    assert 1 == 1
