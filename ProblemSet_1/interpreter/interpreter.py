
def main():
# Input will be like "x y z"
# Where x and z is an integer and y an calculation command
    expression = input("Expression: ").split()
    print("" ,expression[0],expression[1],expression[2])
    int2float(expression)
    #int2float(expression[0],expression[1],expression[2])

    #solution = x y z

def int2float(expression):
    print(expression)




if __name__ == "__main__":
    main()
