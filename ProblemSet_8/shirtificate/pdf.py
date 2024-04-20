from fpdf import FPDF
from fpdf import Align
from PIL import Image

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")

w = 210 #A4 width
h = 297 #A4 height

pdf.set_font("Helvetica", "B", 16)
pdf.add_page() # creates page nr. 1

pdf.cell(0,30,"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') #cell nr.1
# Abstandshalter zwischen Cell Nr 1 und Cell Nr 3

#pdf.cell(0,90,"", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') #cell nr.2
#pdf.set_xy(0, h/2.5)

pdf.image("shirtificate.png", Align.C, y=100, w=180) #when just one param. (w or h) setted, the other gets autom. calculated

#img = Image.open("shirtificate.png")
#width, height = img.size   # Get dimensions
#print(width, height)

#img = img.crop((0, 0, 593, 592)).resize((493, 492))
# 1 pixel = 0.2645833333 mm
# 493 pixel = 130.4395833169 mm
# (210mm - 130.43958mm)/2 = 39.78mm
#pdf.image(img, x=19, y=90, keep_aspect_ratio=True)

pdf.cell(0, 30, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') # cell nr.3

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
