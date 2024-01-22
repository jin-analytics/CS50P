
def main():
# Input will be like "x y z"
# Where x and z is an integer and y an calculation command
    expression = input("Expression: ").split()
   #int2float(expression)
    print (int2float(expression))

def int2float(expression):
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    x = float(x)
    z = float(z)

    if y == '+':
        solution = x + z
        return solution
    elif y == '-':
        solution = x - z
        return solution
    elif y == '*':
        solution = x * z
        return solution
    elif y == '/':
        solution = x / z
        return solution
    else:
        print("Not a supported math comband")






if __name__ == "__main__":
    main()
