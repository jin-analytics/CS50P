from fpdf import FPDF
from PIL import Image

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World!")

img = Image.open("shirtificate.png")
pdf.image(img, x=100, y=100)

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
