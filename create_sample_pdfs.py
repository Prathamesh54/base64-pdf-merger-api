from reportlab.pdfgen import canvas

def make_pdf(path, text):
    c = canvas.Canvas(path)
    c.setFont("Helvetica", 20)
    c.drawString(100, 700, text)
    c.showPage()
    c.save()

make_pdf("sample1.pdf", "This is Sample PDF 1")
make_pdf("sample2.pdf", "This is Sample PDF 2")
print("Created sample1.pdf and sample2.pdf")
