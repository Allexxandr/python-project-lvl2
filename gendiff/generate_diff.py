from gendiff.tools.parse_file import get_dict_from_file
from gendiff.tools.diff import diff
from gendiff.tools.formatter import format_diff


def generate_diff(path_file1, path_file2, format_name='stylish'):
    dict1 = get_dict_from_file(path_file1)
    dict2 = get_dict_from_file(path_file2)

    diff_res = diff(dict1, dict2)
    return format_diff(diff_res) 
