import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']

participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def main():
    if len(sys.argv) == 2:
        mark()
    return

def mark():
    a = sys.argv[1]
    if a  == 'call_center':
        print(call_center())
    elif a == 'potential_clients':
        print(potential_clients())
    elif a == 'loyalty_program':
        print(loyalty_program())
    else:
        print('Unknown command')

def call_center():
    return list(set(clients) - set(recipients))

def potential_clients():
    return list(set(participants) - set(clients))

def loyalty_program():
    return list(set(clients) - set(participants))

if __name__ == "__main__":
    main()
