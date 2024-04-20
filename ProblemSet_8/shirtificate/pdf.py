from fpdf import FPDF
from fpdf import Align
from PIL import Image

name = input("Name: ")

class PDF(FPDF(orientation="P", unit="mm", format="A4")):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(
            width,
            9,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )


pdf.set_font("Helvetica", "B", 16)
pdf.add_page() # creates page nr. 1
pdf.cell(0,30,"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') #cell nr.1

pdf.image("shirtificate.png", Align.C, y=100, w=180) #when just one param. (w or h) setted, the other gets autom. calculated

pdf.set_text_color(0, 50, 50)
pdf.cell(0, 30, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C') # cell nr.3

#pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", h=pdf.eph/2, w=pdf.epw/2)
pdf.output("pdf-with-image.pdf")
