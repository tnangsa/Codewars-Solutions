def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    
    # get square root
    root = sq ** 0.5
    
    # check to see if its a whole number
    if root % 1 == 0:
        # if it is, add 1 to root and square it
        return (root + 1) ** 2
    
    # if not, return -1
    return -1
​