
def delete_many(string, rms):
    """
    Takes a string and a list of strings to delete.
    If the list of strings are all single characters,
    they can be passed as a single string (e.g., "[]() ").
    """

    for rm in rms:
        string = string.replace(rm, '')
    return string


def replace_pairs(string, args, repls):
    """
    Takes a string, a substring to replace, and a paired replacement.
    Equivalent to multiple string.replace() calls.
    """
    if len(args) != len(repls):
        raise KeyError("Find and replace lists must be the same length!")
    else:
        for i in range(0, len(args)):
            string = string.replace(args[i], repls[i])
    return string