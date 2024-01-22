
def main():
# Input will be like "x y z"
# Where x and z is an integer and y an calculation command
    expression = input("Expression: ").split()
    print("vor join" ,expression)
    command = expression[1]
    expression = 'f./command'.join(expression)
    print("nach join" ,expression)
   # int2float(expression)

    #solution = x y z

def int2float():
    print(expression)




if __name__ == "__main__":
    main()
