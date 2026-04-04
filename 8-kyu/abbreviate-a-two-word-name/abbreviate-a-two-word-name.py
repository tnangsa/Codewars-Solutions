def abbrev_name(name):
    name_parts = name.split()
    
    first_initial = name_parts[0][0].upper()
    last_initial = name_parts[1][0].upper()
    
    return f"{first_initial}.{last_initial}"