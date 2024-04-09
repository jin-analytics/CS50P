from fpdf import FPDF
from PIL import Image

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 24)
pdf.cell(40, 10, "CS50 Shirtificate")

img = Image.open("shirtificate.png")
img = img.crop((0, 0, 593, 592)).resize((493, 492))
pdf.image(img, x=20, y=40, keep_aspect_ratio=True)
pdf.cell(40, 150, "Jakob Niedenhoff took CS50")

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
