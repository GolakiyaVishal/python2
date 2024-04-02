import sys

if __name__ == '__main__':
    n = -1
    phonebook = {}

    for line in sys.stdin:
        if n == -1:
            n = int(line)
        else:
            if n >= 1:
                name, contact = line.strip().split(' ')
                phonebook[name] = contact
                n -= 1
            else:
                if line.strip() in phonebook:
                    sys.stdout.write(f'{line.strip()}={phonebook[line.strip()]}\n')
                else:
                    sys.stdout.write('No found\n')
