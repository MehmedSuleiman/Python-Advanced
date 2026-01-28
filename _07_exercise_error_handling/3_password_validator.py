class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

SPECIAL_CHARACTERS = [ "@", "*", "&"]

def password_validator(password, SPECIAL_CHARACTERS):
    only_digets = password.isdigit()
    only_letters = password.isalpha()
    return only_digets or only_letters or all(ch in SPECIAL_CHARACTERS for ch in password)

while True:
    password = input()
    if password == 'Done':
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

#    if password.isdigit() or password.isalpha() or all(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if password_validator(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
