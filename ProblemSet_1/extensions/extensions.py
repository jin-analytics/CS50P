# input something like xyz.jpg, where the suffix has a spezific extension
# lower the input and remove given spaces
filelist =  input("File name: ").lower().replace(" ","")
#filelist = filelist.split(".")
# Get the last element of the list with [-N:], where "N" equals the number of last entrees
#N = 1
ext = filelist
#print(ext)


match filelist:
    case "gif" | "jpeg" | "png" | "jpg":
#if ext[1] == "gif" or "jpeg" or "png" or "jpg":
     #   if ext == "jpeg":
            print("image/jpg")
    #    else:
            print("image/", ext, sep='')
    case "txt":
            print("text/plain")
    case "zip" | "pdf":
            print("application/", ext, sep='')
    case "test":
            print ("test geht")
    case _:
            print("application/octet-stream")
