def flatten_list(a, result=None):
    if result is None:
        result = dict()

    for x in a:
        if isinstance(a[x], dict):
            flatten_list(a[x], result)
        else:	
            result[x]=a[x]

    return result



a={'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
print flatten_list(a)
