def remove_exclamation_marks(s):
    #your code here
    new_string = ""
    for i in s:
        if i != '!':
            new_string += i
    return new_string
        