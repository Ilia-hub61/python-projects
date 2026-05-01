from random import randint

class Research:
    def __init__(self, path):
        self.path = path
        self.reader = self.file_reader()
        self.calc = self.Calculations(self.reader)
        self.analyt = self.Analytics(self.reader)
        
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
        def __init__(self, data):
            if not data:
                raise ValueError("Empty data provided")
            self.data = data
            
        def counts(self):
            head = 0
            tail = 0
            for i in self.data:
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
    
    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)

        def predict_random(self, k):
            if k <= 0:
                raise ValueError("Number of predictions must be positive")
            dict_or = {0: [0, 1], 1: [1, 0]}
            res = []
            for i in range(k):
                res.append(dict_or[randint(0, 1)])
            return res
        
        def predict_lastself(self):
            if not self.data:
                raise ValueError("No data available for prediction")
            return self.data[-1]
        
        def save_file(self, output, data):
            try:
                with open(output, "w") as file:
                    file.write(data)
            except (FileNotFoundError, PermissionError) as e:
                raise e
            except Exception as e:
                raise Exception(f"Error saving file: {e}")
