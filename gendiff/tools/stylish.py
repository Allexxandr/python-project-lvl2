import json

def format_diff(diff, format_type):
    
    if format_type == 'stylish':
        return format_stylish(diff)
    elif format_type == 'plain':
        return format_plain(diff)
    elif format_type == 'json':
        return format_json(diff)
    raise 'Format not found!'


def format_dict(info, indent):
    if type(info) is dict:
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

def format_stylish(gendiff, tree = 0):
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



def format_plain(diff, path=''):
    result = []
    for info in diff:
        if info['mode'] == 'added':
            tree_path = path + info['name']
            diff = (
                f"Property '{tree_path}' was added "
                f"with value: {info['data']}"
            )
            result.append(diff)
        if info['mode'] == 'deleted':
            tree_path = path + info['name']
            diff = "Property '{}' was removed".format(tree_path)
            result.append(diff)
        if info['mode'] == 'have children':
            tree_path = path + info['name'] + '.'
            diff = format_plain(info['children'], tree_path)
            result.append(diff)
        if info['mode'] == 'changed':
            tree_path = path + info['name']
            diff = (
                f"Property '{tree_path}' was updated. "
                f"From {info['data before']} to {info['data after']}"
            )
            result.append(diff)
    return '\n'.join(result)

def format_json(diff):
    return json.dumps(diff)



