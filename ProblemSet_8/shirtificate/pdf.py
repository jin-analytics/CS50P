from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", keep_aspect_ratio=True)
pdf.output("pdf-with-image.pdf")
