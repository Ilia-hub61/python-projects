def read():
    with open('ds.csv', 'r') as f:
        with open('ds.tsv', 'w') as f_o:
            f_o.write(f.read().replace('",', '"\t')
                              .replace('false,', 'false\t')
                              .replace('true,', 'true\t'))

if __name__ == '__main__':
    read()
