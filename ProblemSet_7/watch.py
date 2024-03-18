#<iframe width="560" height="315"
#src="https://www.youtube.com/embed/xvFZjo5PgG0?si=PBf3-vT-bKafDGvb"
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
#
#
