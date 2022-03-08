def format_dict(info, indent):
    if isinstance(info, dict):
        indent = indent + '   '
        result = '{\n'
        for key in info.keys():
            formatted = format_dict(info[key], indent)
            result += indent + ' ' + key + ':' + formatted + '\n'
        result += indent[:-2] + '}'

    elif info is False:
        result = 'false'
    elif info is True:
        result = 'true'
    elif info is None:
        result = 'null'
    else:
        result = str(info)
    return result


def format_stylish(gendiff, tree=0):  # noqa: C901
    result = '{\n'
    indent = ' '
    for i in range(tree):
        indent += ' '
    gendiff.sort(key=lambda x: x['name'])
    for info in gendiff:
        if info['mode'] == 'have children':
            data = format_stylish(info['children'], tree + 1)
            result += f" {info['name']}: {data}\n"
        if info['mode'] == 'not changed':
            data = format_dict(info['data'], indent)
            result += f"    {info['name']}: {data}\n"
        if info['mode'] == 'added':
            data = format_dict(info['data'], indent)
            result += f"  + {info['name']}: {data}\n"
        if info['mode'] == 'deleted':
            data = format_dict(info['data'], indent)
            result += f"  - {info['name']}: {data}\n"
        if info['mode'] == 'changed':
            data = format_dict(info['data before'], indent)
            result += f"  - {info['name']}: {data}\n"
            data = format_dict(info['data after'], indent)
            result += f"  + {info['name']}: {data}\n"

    result += indent[:-2] + '}'

    return result
