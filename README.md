# mini_programs
small helpful snippets that I coded for personal use

## PDF Page Counter
Python script that traverses all PDF files inside the current directory and lists out their filenames and number of pages. Requires PDFMiner package (on Windows, pip or conda install pdfminer). If you have a large number of files, you might want to pipe the output to a file instead of view it on screen. One workflow is to use a delimiter of your choice between filename and page number, pipe the output to a text file and do Open Special in Excel as a delimited file (e.g. tab separated values, or semicolons. Using comma or space as a separator is usually not feasible as PDF files might have those in their titles already). Currently the default separator between filename and number of pages is set as a semicolon.
