# mini_programs
Short useful programs that I coded for personal use

## PDF Page Counter
Python script that traverses all PDF files inside the current directory and lists out their filenames and the number of pages in each.

#### Example use case
For a course at university, we were given a folder that had several hundred research papers on a theme (chatbots), and had to review any three of them. To get a quick sense of the scope covered by each paper, I wrote this program to know the length of each paper. This allowed selection of a good mix of short and long papers for the literature review. 

#### Usage
Open terminal/command prompt, go to the folder where the PDF files are located, and simply run:

`python PDF_page_counter.py`

The terminal will output the names of all PDF files (filenames, not PDF titles) and the number of pages each has.

You can also redirect the output to a file for later analysis (see technical notes below for examples):

`python PDF_page_counter.py > filelist.txt`


#### Technical notes:
Requires PDFMiner package. On Windows, pip or conda install pdfminer. If you have a large number of PDF files, you might want to pipe the output to a file instead of view it on screen/stdout. One workflow is:
1. Use a delimiter of your choice between the filename and page number, currently it's a semi-colon (line 33 of the code: replace the semi-colon in `sep = ';'` )
2. Run the program, piping the output to a text file 
3. Open Special the above in Excel as a delimited file (e.g. tab separated values, or semicolons)

Note: Using comma or space as a separator is usually not feasible as PDF files might have those in their titles already. The current default separator between the filename and its number of pages is set as a semicolon; it works well for most use-cases.
