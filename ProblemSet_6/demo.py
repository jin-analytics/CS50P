con = []

with open('test.txt','r') as f:
    content = f.readlines()

    for lines in content:
        con = con.append(lines)
