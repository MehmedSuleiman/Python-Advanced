class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

MIN_LENGTH = 4
VALID_DOMAINS = ["com", "bg", "net", "org"]

while True :
    line = input()
    if line == "End":
        break

    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")

    len_name = line.split("@")[0]
    if len(len_name) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    email_domain = line.split(".")[-1]

    if email_domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid" )


