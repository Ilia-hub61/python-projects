import sys

s = sys.argv

def main():
    if len(sys.argv) == 2:
        names()
    return

def names():
    with open(s[1], 'r') as file:
        with open('employees.tsv', 'w') as employess:
            employess.write("Name\tSurname\tE-mail\n")
            for email in file:
                name_parts = email.split('@')[0].split('.')
                name, surname = name_parts
                name = name.capitalize()
                surname = surname.capitalize()
                employess.write(f"{name}\t{surname}\t{email}")


if __name__ == "__main__":
    main()
