import os.path
from reportlab.lib.pagesizes import landscape, letter, A4
from reportlab.lib.units import inch, cm

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Image

from PyPDF2 import PdfWriter, PdfReader

parts = []

img_files = ['src/test1.jpg', 'src/test2.jpg', 'src/test3.jpg', 'src/test4.png']

doc = SimpleDocTemplate("generated/images.pdf", pagesize=A4)
for img in img_files:
  parts.append(Image(img, width=19.00*cm, height=12*cm, kind='proportional'))

doc.build(parts)

# Merge some arbitrary PDF and newly created images.pdf
pdf_files = ['src/a4-h.pdf', 'src/a4-l.pdf', 'generated/images.pdf'];
output = PdfWriter()

for pdf_file in pdf_files:
  input_pdf = PdfReader(open( pdf_file, "rb"))
  for i in range(len(input_pdf.pages)): 
    output.add_page(input_pdf.pages[i])

outputStream = open('generated/merged.pdf', "wb")
output.write(outputStream)
outputStream.close()
