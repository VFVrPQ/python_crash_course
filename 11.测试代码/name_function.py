def get_formatted_name(first, last, middle=''):
    '''生成简洁的姓名'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

"""
def get_formatted_name(first, middle, last):
    '''生成简洁的姓名'''
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
"""