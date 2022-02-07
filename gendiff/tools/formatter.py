def format_diff(gendiff):
    result = '{\n'
    gendiff.sort(key=lambda x: x['name'])
    
    for info in gendiff:
        
        if info['mode'] == 'not changed':
            
            result += f"  {info['name']}: {info['data']}\n"
        if info['mode'] == 'added':
     
            result += f"  + {info['name']}: {info['data']}\n"
        if info['mode'] == 'deleted':
    
            result += f"  - {info['name']}: {info['data']}\n"
        if info['mode'] == 'changed':
           
            result += f"  - {info['name']}: {info['data before']}\n"
            
            result += f"  + {info['name']}: {info['data after']}\n"

        
    
    return result + '}'