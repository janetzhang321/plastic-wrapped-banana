#WORKING
def hasRequirements(password):
    hasLower = [char for char in list(password) if char == char.lower() ]
    
    hasUpper = [char for char in list(password) if char == char.upper() ]
    hasNumber = [char for char in list(password) if char.isdigit() and int(char) in range(0, 10)]  
    
    if (hasLower and hasUpper and hasNumber):
        return True
    else:
        return False

