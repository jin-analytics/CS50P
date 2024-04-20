from fpdf import FPDF
from PIL import Image

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")

w = 210 #A4 width
h = 297 #A4 height

pdf.set_font("Helvetica", "B", 16)
pdf.add_page() # creates page nr. 1
pdf.cell(0,30,"CS50 Shirtificate", align = 'C', )

pdf.cell(0,30,"____________", border = 1 , align = 'C')


img = Image.open("shirtificate.png")
img = img.crop((0, 0, 593, 592)).resize((493, 492))
pdf.image(img, x=20, y=90, keep_aspect_ratio=True)
pdf.cell(0, 30, f"{name} took CS50", new_x="Center", new_y="NEXT", align='C')

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
