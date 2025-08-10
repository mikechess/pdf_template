from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt='Hello There!', ln=1, align='L')

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt='Hi There!', ln=1, align='L')

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt='Hello There!', ln=1, align='L')

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt='Hi There!', ln=1, align='L')

pdf.output('output.pdf')




