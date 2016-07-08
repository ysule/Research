from pyPdf import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open(raw_input("Enter pdf file name (example.pdf):"), "rb"))

for i in xrange(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
