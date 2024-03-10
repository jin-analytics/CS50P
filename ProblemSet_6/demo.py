con = []

with open('test.txt','r') as f:
    content = f.readlines()

    for line in content:
        #con = con.append(lines)
        #print('...',line)
        #print(line[0])
        pass
        if line == '\n':
            #print('check')
            pass
        elif line[0] == '#':
            pass
            print('check2')
