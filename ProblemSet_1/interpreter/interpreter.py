
def main():
# Input will be like "x y z"
# Where x and z is an integer and y an calculation command
    expression = input("Expression: ").split()
    #print("was geht" ,expression[0],expression[1],expression[2])
    int2float(expression)
    #int2float(expression[0],expression[1],expression[2])
    print(expression)
    #solution = x y z

def int2float(expression):
    print(expression)
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    x = float(x)
    z = float(z)

    if y == '+':
        expression = x + z
    elif y == '-':
        expression = x - z
    elif y == '*':
        expression = x * z
    elif y == '/':
        expression = x / z
    else:
        print("Not a supported math comband")

    return expression




if __name__ == "__main__":
    main()
