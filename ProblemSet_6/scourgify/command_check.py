
command_check(command_line_input, accepted_value, filetype)

def command_check(i,a):
        accepted_value = a

        if len(sys.argv) < accepted_value:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > accepted_value:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
