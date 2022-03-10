from gendiff.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    return os.path.join(os.getcwd(), 'fixtures', file_name)


def test_gendiff():
    dict1 = get_fixture_path('file1.json')
    dict2 = get_fixture_path('file2.json')
    correct_answer_path_stylish = get_fixture_path('correct_answer_stylish')
    with open(correct_answer_path_stylish) as f:
        correct_answer_data_stylish = f.read()

    correct_answer_path_plain = get_fixture_path('correct_answer_plain')
    with open(correct_answer_path_plain) as f:
        correct_answer_data_plain = f.read()

    assert generate_diff(dict1, dict2) == correct_answer_data_stylish
    assert generate_diff(dict1, dict2, format_type='plain') == correct_answer_data_plain  # noqa: E501
