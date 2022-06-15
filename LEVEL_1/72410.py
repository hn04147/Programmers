def solution(new_id):
    new_id = new_id.lower()
    
    id = ''
    for c in new_id:
        if c.isalnum() or c in '-_.':
            id += c
    print(id)
    
    while '..' in id:
        id = id.replace('..', '.')
    print(id)
    
    if id[0] == '.' and len(id) > 1: 
        id = id[1:]
    if id[-1] == '.':
        if len(id) > 1:
            id = id[:-1]
        else:
            id = ''
    print(id)
    
    if id == '': id = 'a'
    print(id)
    
    if len(id)>15: 
        id = id[:15]
        if id[-1] == '.':
            id = id[:14]
    print(id)
    
    if len(id) == 1: id = id + id[0] + id[0]
    elif len (id) == 2: id = id + id[-1]
    print(id)
    return id
