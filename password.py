#WORKING
def hasRequirements(password):
    hasLower = [char for char in list(password) if char == char.lower() and not char.isdigit() ]
    print hasLower
    hasUpper = [char for char in list(password) if char == char.upper() and not char.isdigit() ]
    print hasUpper
    hasNumber = [char for char in list(password) if char.isdigit() and int(char) in range(0, 10)]  
    print hasNumber
    if (hasLower and hasUpper and hasNumber):
        return True
    else:
        return False

#testing
print hasRequirements("PASSWORRDDD1")
print hasRequirements("yayforfreeperiods2")
print hasRequirements("softdev")
print hasRequirements("Ineedfood123")


#max strength is 5
def passwordStrength(password):
    hasLower = [char for char in list(password) if char == char.lower() ]
    hasUpper = [char for char in list(password) if char == char.upper() ]
    hasNumber = [char for char in list(password) if char.isdigit() and int(char) in range(0, 10)]
    hasSymbol = [char for char in list(password) if char in "!@#$%^&*?"]

    strength = 0
    if (hasLower):
        strength += 1
    if (hasUpper):
        strength += 1
    if (hasNumber):
        strength += 1
    if (hasSymbol):
        strength += 1
    if (len(password) > 12):
        strength += 1

    return strength
