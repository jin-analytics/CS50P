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
        self.cell(0,30,"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", border = 1, align = 'C')

pdf = PDF()
pdf.output("pdf-file")
