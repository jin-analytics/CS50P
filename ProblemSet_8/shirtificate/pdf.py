from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", x=20, y=60)
pdf.output("pdf-with-image.pdf")
