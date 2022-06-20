def valid(passwort: str) -> bool:
    if len(passwort) < 8:
        return False
    #TODO: mehr Kriterien implementieren (Sonderzeichen, Großbuchstaben, Zahlen, ...)
    return True

username = input("Username: ")
passwort = input("Passwort: ")

while valid(passwort) == False:
    passwort = input("Passwort: ")

print(username)
print(passwort)