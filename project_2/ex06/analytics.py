from random import randint
import logging
import requests
import json

logging.basicConfig(filename='analytics.log', level=logging.INFO, format='%(asctime)s %(message)s')

class Research:
    def __init__(self, path):
        logging.info('Initializing Research with path: %s', path)
        self.path = path
        self.reader = self.file_reader()
        self.calc = self.Calculations(self.reader)
        self.analyt = self.Analytics(self.reader)

    def file_reader(self, has_header=True):
        logging.info('Reading file: %s', self.path)
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
            logging.error('File not found: %s', self.path)
            raise FileNotFoundError(f"File {self.path} not found")
        except PermissionError:
            logging.error('Permission denied to read: %s', self.path)
            raise PermissionError(f"Permission denied to read {self.path}")
            
        if not res:
            logging.error('No valid data found in file: %s', self.path)
            raise ValueError("No valid data found in file")
            
        logging.info('File read successfully, %d rows', len(res))
        return res

    def send_telegram(self, bot_token, message):
        logging.info('Sending message to Telegram: %s', message)
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": 1662609079,
            "text": message
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                logging.info('Telegram message sent successfully')
            else:
                logging.error('Failed to send Telegram message: %s', response.text)
        except Exception as e:
            logging.error('Exception during Telegram send: %s', str(e))

    class Calculations:
        def __init__(self, data):
            logging.info('Initializing Calculations')
            if not data:
                logging.error('Empty data provided to Calculations')
                raise ValueError("Empty data provided")
            self.data = data
            
        def counts(self):
            logging.info('Calculating counts of heads and tails')
            head = 0
            tail = 0
            for i in self.data:
                if i[0] == 1:
                    head += 1
                elif i[1] == 1:
                    tail += 1
            logging.info('Counts: heads=%d, tails=%d', head, tail)
            return head, tail
            
        def fractions(self, b, c):
            logging.info('Calculating fractions')
            if b + c == 0:
                logging.error('Cannot calculate fractions: no data')
                raise ValueError("Cannot calculate fractions: no data")
            summa = b + c
            result = (b / summa * 100, c / summa * 100)
            logging.info('Fractions: %s', result)
            return result
    
    class Analytics(Calculations):
        def __init__(self, data):
            logging.info('Initializing Analytics')
            super().__init__(data)

        def predict_random(self, k):
            logging.info('Predicting random for %d steps', k)
            if k <= 0:
                logging.error('Number of predictions must be positive')
                raise ValueError("Number of predictions must be positive")
            dict_or = {0: [0, 1], 1: [1, 0]}
            res = []
            for i in range(k):
                res.append(dict_or[randint(0, 1)])
            logging.info('Random prediction: %s', res)
            return res
        
        def predict_lastself(self):
            logging.info('Predicting last observation')
            if not self.data:
                logging.error('No data available for prediction')
                raise ValueError("No data available for prediction")
            return self.data[-1]
        
        def save_file(self, output, data):
            logging.info('Saving report to file: %s', output)
            try:
                with open(output, "w") as file:
                    file.write(data)
                logging.info('Report saved successfully')
            except (FileNotFoundError, PermissionError) as e:
                logging.error('Error saving file: %s', str(e))
                raise e
            except Exception as e:
                logging.error('Unexpected error saving file: %s', str(e))
                raise Exception(f"Error saving file: {e}")
