def diff(dict1, dict2):
    result = []
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        info = {'name': key}
        if key not in dict1:
            info['mode'] = 'added'
            info['data'] = dict2[key]
        elif key not in dict2:
            info['mode'] = 'deleted'
            info['data'] = dict1[key]
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            info['mode'] = 'have children'
            info['children'] = diff(dict1[key], dict2[key])
        elif dict1[key] == dict2[key]:
            info['mode'] = 'not changed'
            info['data'] = dict1[key]
        else:
            info['mode'] = 'changed'
            info['data before'] = dict1[key]
            info['data after'] = dict2[key]
        result.append(info)
    return result
