def checkNotNull(params):
    """
    Check if arguments are non Null
    
    Arguments:
        params {array}
    """
    for value in params:
        if value == None:
            return False
    return True


# print(checkNotNull([1, "abc", 0, None]))
