import sys

class Research:
    def __init__(self, path):
        self.path = path
        self.calc = self.Calculations()
        
    def file_reader(self, has_header=True):
            
        res = []
        try:
            with open(self.path, "r") as f:
                if has_header:
                    header = next(f).strip()
                    if not header or ',' not in header:
                        raise ValueError("Invalid header format")
                        
                for line_num, line in enumerate(f, 2):
                    line = line.strip()
                    if not line:
                        continue
                        
                    try:
                        numbers = line.split(',')
                        if len(numbers) != 2:
                            raise ValueError(f"Line {line_num}: expected 2 values, got {len(numbers)}")
                            
                        number = list(map(int, numbers))
                        
                        # Проверка, что значения только 0 и 1, и ровно одно из них равно 1
                        if not (number[0] in [0, 1] and number[1] in [0, 1]):
                            raise ValueError(f"Line {line_num}: values must be 0 or 1")
                        if number[0] == number[1]:
                            raise ValueError(f"Line {line_num}: exactly one value must be 1")
                            
                        res.append(number)
                    except ValueError as e:
                        if "invalid literal" in str(e):
                            raise ValueError(f"Line {line_num}: invalid number format")
                        raise e
                        
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.path} not found")
        except PermissionError:
            raise PermissionError(f"Permission denied to read {self.path}")
            
        if not res:
            raise ValueError("No valid data found in file")
            
        return res
        
    class Calculations:
        def counts(self, a):
            if not a:
                raise ValueError("Empty data provided")
            head = 0
            tail = 0
            for i in a:
                if i[0] == 1:
                    head += 1
                elif i[1] == 1:
                    tail += 1
            return head, tail
            
        def fractions(self, b, c):
            if b + c == 0:
                raise ValueError("Cannot calculate fractions: no data")
            summa = b + c
            return b / summa * 100, c / summa * 100

if __name__ == "__main__":
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        data = research.file_reader()
        count = research.calc.counts(data)
        x, y = count
        fract = research.calc.fractions(x, y)
        print(data)
        print(*count)
        print(*fract)
    else:
        print("Error")
