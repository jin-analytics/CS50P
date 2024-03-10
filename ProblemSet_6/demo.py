counter = []

with open('test.txt','r') as f:
    content = f.readlines()

    for line in content:
        pass

        if line == '\n':
            counter.append(1)

        elif line[0] == '#':
            counter.append(1)

    print(len(content) - len(counter))
