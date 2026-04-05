def abbrev_name(name):
    name_parts = name.upper().split()
    
    first_initial = name_parts[0][0]
    last_initial = name_parts[1][0]
    
    return f"{first_initial}.{last_initial}" 