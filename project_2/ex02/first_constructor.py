import sys

class Research:
    def __init__(self, path):
        self.path = path
    def file_reader(self):
        with open(self.path, "r") as f:
            return f.read()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        print(research.file_reader())
    else:
        print("Error")
