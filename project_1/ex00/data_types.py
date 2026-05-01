def data_types():
    a = [0, 'abc', 0.0, True, [1, 2, 3], {0: 'man'}, (1, 2, 3), set()]
    s = '['
    for i in range(len(a) - 1):
        s += str(type(a[i]).__name__) + ', '
    print(f"{s}{str(type(a[-1]).__name__) + ']'}")

if __name__ == '__main__':
    data_types()
