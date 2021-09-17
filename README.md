# mini_programs
For small helpful snippets that I coded for personal use

## PDF Page Counter
Traverses all PDF files inside the current directory and lists out their filenames and number of pages. Requires PDFMiner package. If have large list of files, might want to use delimiter of your choice between filename and page number, pipe output to a text file and open special in Excel as a delimited file (e.g. tab separated values, or semicolons. Using comma or space as separator not feasible coz files might have those in their titles already). Currently the default separator between filename and number of pages is set as a semicolon.
