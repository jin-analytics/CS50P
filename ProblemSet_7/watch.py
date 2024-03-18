#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=PBf3-vT-bKafDGvb"
#title="YouTube video player" frameborder="0"
#allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
#allowfullscreen></iframe>


# implement a function called parse():
# - that expects a str of HTML as input,
# - extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
# - and returns its shorter,
# - shareable youtu.be equivalent as a str
#
# Possible inputs:
# input: http://youtube.com/embed/xvFZjo5PgG0
# input: https://youtube.com/embed/xvFZjo5PgG0
# input: https://www.youtube.com/embed/xvFZjo5PgG0
# Assume that the value of src will be surrounded by double quotes
# If the input does not contain any such URL at all, return None


import re
import sys

#{sys.argv[1:]}
def main():
    print(parse(input("HTML: ")))


def parse(s):
    #s = re.split(r"^\w[a-z0-9\"/.]*=+[a-z0-9\"/.]*$")
    #=(/w[\":/.?-])
    s = re.search(r"^(/w[ \<\>\"\:\.\?\-\=])+src$", s)
    print('found: ',s)


...


if __name__ == "__main__":
    main()
