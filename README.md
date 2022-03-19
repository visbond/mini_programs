# mini_programs
small helpful snippets that I coded for personal use

## PDF Page Counter
Python script that traverses all PDF files inside the current directory and lists out their filenames and number of pages.

#### Example use case
For a course at university, I had to review 3 research papers, out of several hundred. To get a quick sense of the scope covered by each paper, I wrote this program to get an idea of their respective lengths. It allowed selection of a good mix of short and long papers for the literature review. 

#### Technical notes:
Requires PDFMiner package. On Windows, pip or conda install pdfminer. If you have a large number of PDF files, you might want to pipe the output to a file instead of view it on screen/stdout. One workflow is:
1. Use a delimiter of your choice between the filename and page number (line 33 of the code)
2. Run the program, piping the output to a text file 
3. Open Special the above in Excel as a delimited file (e.g. tab separated values, or semicolons)

Note: Using comma or space as a separator is usually not feasible as PDF files might have those in their titles already. Currently the default separator between filename and number of pages is set as a semicolon.
