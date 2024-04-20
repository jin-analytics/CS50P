from fpdf import FPDF
from fpdf import Align

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_font("Helvetica", "B", 16)
pdf.add_page() # creates page nr. 1
pdf.cell(0,30,"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') #cell nr.1

pdf.allow_images_transparency = True
im = pdf.image("shirtificate.png", Align.C, y=90, w=180) #when just one param. (w or h) setted, the other gets autom. calculated

pdf.set_text_color(255, 255, 255)
pdf.cell(0, 30, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') # cell nr.3

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
