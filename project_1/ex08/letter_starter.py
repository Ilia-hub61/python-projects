import sys

s = sys.argv

def main():
    if len(sys.argv) == 2:
        print(names(s[1]))
    return

def names(email):
    with open("employees.tsv", 'r') as file:
        for line in file:
            elements = line.split("\t")
            element = elements[2].split("\n")
            if element[0] != email:
                continue
            else:
                return f"Dear {elements[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires."

if __name__ == "__main__":
    main()
