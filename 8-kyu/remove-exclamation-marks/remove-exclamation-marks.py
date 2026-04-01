def remove_exclamation_marks(s):
    #your code here
    new_string = ""
    for x in s:
        if x != '!':
            new_string += x
    return new_string