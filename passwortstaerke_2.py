def valid(passwort: str, minNumbers: int) -> bool:
    conditionLength = False
    conditionNumbers = False
    conditionWhiteSpace = True
    
    if len(passwort) > 8:
        conditionLength = True

    counter = 0
    for p in passwort:
        if p.isdigit():
            counter += 1

    if counter >= minNumbers:
        conditionNumbers = True

    for p in passwort:
        if p == ' ':
            conditionWhiteSpace = False
            break
    
    return conditionLength and conditionNumbers and conditionWhiteSpace

username = input("Username: ")
passwort = input("Passwort: ")

minNumbers = 3
while valid(passwort, minNumbers) == False:
    passwort = input("Passwort: ")

print(username)
print(passwort)
