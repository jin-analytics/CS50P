
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
    elif y == '-':
        solution = x - z
    elif y == '*':
        solution = x * z
    elif y == '/':
        solution = x / z
    else:
        print("Not a supported math comband")
    # round the soultion to 1 decimal point and then returns it to main function
    solution = round(solution,1)
    return solution

if __name__ == "__main__":
    main()
