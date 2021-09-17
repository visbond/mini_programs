# to traverse all PDF files in a folder and count their number of pages, uses the PDFMiner package
# useful when have a dump of a lot of reading material and want to prioritise it based on length
# I made this when a course asked us to read and summarise a few research papers from a collection of hundreds

import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1


def PDFPageCount(filename):
    # print("DEBUG entered PDFPageCount() with", filename)
    with open(filename, 'rb') as file:
        parser = PDFParser(file)
        document = PDFDocument(parser)

        # Notes on code below: document.catalog is a dictionary with many properties of the PDF
        # many values are listed as PDF objects rather than actual values. They need to be resolved
        # via the resolve1 function to convert to exact value (often another dictionary)

        # print("DEBUG", document.catalog)
        pages = document.catalog['Pages']
        pagecount = resolve1(pages)['Count']
    return pagecount


if __name__ == '__main__':
    print("Current working directory is ", os.getcwd())
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        if filename.endswith(".pdf") or filename.endswith(".PDF"):
            print(filename, PDFPageCount(filename), sep = ';')

        # is satisfying to account for all logical branches, even if currently empty (<something zen about finding fullness in emptiness here>
        else:
            continue
