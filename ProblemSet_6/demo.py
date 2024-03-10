con = []

with open('test.txt','r') as f:
    content = f.readlines()

    for line in content:
        #con = con.append(lines)
        print('...',line)
        if line == '\n':
            print('check')
        elif line[1:] == '#':
            print('check2')
