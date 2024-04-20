from fpdf import FPDF
from PIL import Image

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
#pdf.cell(40, 50, "CS50 Shirtificate")
pdf.cell(Center, Top, "CS50 Shirtificate")
#XPos(Center)


img = Image.open("shirtificate.png")
img = img.crop((0, 0, 593, 592)).resize((493, 492))
pdf.image(img, x=20, y=90, keep_aspect_ratio=True)
pdf.cell(100, 300, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align='C')

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
