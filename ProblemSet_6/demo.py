con = []

with open('test.txt','r') as f:
    content = f.readlines()

    for line in content:
        #con = con.append(lines)
        #print('...',line)
        print('...',content[line])
