import sys

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit2 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
al = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

s = sys.argv

def main():
    if len(s) == 4:
        if s[1] == 'encode':
            encode()
        elif s[1] == 'decode':
            decode()
    return

def encode():
    itog = ''
    for i in s[2]:
        if i in al:
            print("The script does not support your language yet")
            return
        else:
            if i in alfavit:
                place = alfavit.find(i)
                nplace = place + int(s[3])
                itog += alfavit[nplace]
            elif i in alfavit2:
                place = alfavit2.find(i)
                nplace = place + int(s[3])
                itog += alfavit2[nplace]
            else:
                itog += i
    print(itog)

def decode():
    itog = ''
    for i in s[2]:
        if i in al:
            print("The script does not support your language yet")
            return
        else:
            if i in alfavit:
                place = alfavit.find(i)
                nplace = place - int(s[3])
                itog += alfavit[nplace]
            elif i in alfavit2:
                place = alfavit2.find(i)
                nplace = place - int(s[3])
                itog += alfavit2[nplace]
            else:
                itog += i
    print(itog)


if __name__ == "__main__":
    main()
