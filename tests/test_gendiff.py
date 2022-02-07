from gendiff.generate_diff import generate_diff
import os
import json

def get_fixture_path(file_name):
    return os.path.join(os.getcwd(), 'fixtures', file_name)

def test_gendiff():
    dict1 = get_fixture_path('file1.json')
    dict2 = get_fixture_path('file2.json')
    correct_answer_path = get_fixture_path('correct_answer')
    with open(correct_answer_path) as f:
        correct_answer_data = f.read()
        
       
    print(generate_diff(dict1, dict2))
    print(correct_answer_data)
    assert generate_diff(dict1, dict2) == correct_answer_data


    