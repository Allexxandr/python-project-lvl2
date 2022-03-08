def format_plain(diff, path=''):
    result = []
    for info in diff:
        if info['mode'] == 'added':
            tree_path = path + info['name']
            diff = (
                f"Property '{tree_path}' was added "
                f"with value: {make_change(info['data'])}"
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
                f"From {make_change(info['data before'])} to {make_change(info['data after'])}"  # noqa: E501
            )
            result.append(diff)
    return '\n'.join(result)


def make_change(data):
    if type(data) is dict or type(data) is list:
        result = '[complex value]'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    elif type(data) is str:
        result = "'{}'".format(data)
    else:
        result = '{}'.format(data)
    return result
