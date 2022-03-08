from gendiff.format.stylish import format_stylish
from gendiff.format.plain import format_plain
from gendiff.format.json import format_json


def format_diff(diff, format_type):
    if format_type == 'stylish':
        return format_stylish(diff)
    elif format_type == 'plain':
        return format_plain(diff)
    elif format_type == 'json':
        return format_json(diff)
    raise 'Format not found!'
