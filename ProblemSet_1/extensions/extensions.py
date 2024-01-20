# input something like xyz.jpg, where the suffix has a spezific extension
# lower the input and remove given spaces
ext =  input("File name: ").lower().replace(" ","")
ext = ext.split(".")
# Get the last elements of the list with [-N:], where "N" equals the number of last entrees
N = 1
ext = ext[-N:]
# case cant see a list, so the list entree has to be defined as a single string (at this example)
ext = ext[0]

match ext:
    case "gif" | "png":
            print("image/", ext, sep='')
    case "jpeg" | "jpg":
            print("image/jpeg", sep='')
    case "txt":
            print("text/plain")
    case "zip" | "pdf":
            print("application/", ext, sep='')
    case "test":
            print ("test geht")
    case _:
            print("application/octet-stream")
