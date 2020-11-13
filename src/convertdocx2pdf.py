from reportlab.lib.pagesizes import B5
import PyPDF2

from reportlab.pdfgen import canvas


from docx import Document


def last_line(i=int, pdfname=str):

    pdfFile = open(pdfname, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    count = 0
    try:
        page = pdfReader.getPage(i).extractText().split('\n')
    except IndexError:
        return None
    for l in range(len(page)-1, 0, -1):
        t = page[l]
        if len(t) > 1:
            lineToMatch = page[l]
            # print(lineToMatch)
            return [lineToMatch, count]
        count += 1

    pdfFile.close()


def convertDocxToPDF(docx_name=str, pdf_name=str, final_pdf_name=str):
    doc = Document(docx_name)

    textLines = []
    count = 0
    for i in doc.paragraphs:
        count += 1
        textLines.append(i.text)

    pdf = canvas.Canvas(final_pdf_name)

    text = pdf.beginText(30, 800)

    #text.setFont("Courier", 12)
    i = 0
    last_tuple = last_line(0, pdf_name)

    flag = 0

    for every_line in textLines:

        if last_tuple[0] in every_line or flag == 1:
            flag = 1
            if last_tuple[1] > 0:
                last_tuple[1] -= 1
                text.textLine(every_line)
                continue
            flag = 0
            pdf.drawText(text)
            pdf.showPage()

            text = pdf.beginText(30, 800)
            text.setFont("Courier", 12)
            i += 1
            last_tuple = last_line(i, pdf_name)
            if last_tuple == None:
                break

        else:
            print(every_line)
            text.textLine(every_line)

    pdf.drawText(text)
    pdf.showPage()
    pdf.save()
