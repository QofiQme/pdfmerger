--------------------------------
Merge Multiple PDFs with Python
--------------------------------
This Python script allows you to select multiple PDF files using a file dialog box and combine them into a single PDF document using the PyPDF2 library. The merged PDF file is saved in the same directory as the first selected PDF file, with the name "merged.pdf".

-------------------------------
Dependencies
-------------------------------
The script requires the following dependencies:

os
tkinter
PyPDF2
You can install PyPDF2 using pip by running the following command in your terminal or command prompt:

'pip install PyPDF2'

-------------------------------
How to Use
-------------------------------
Save the script to a Python file (e.g., merge_pdfs.py).
Make sure that the script's dependencies are installed (see above).
Run the script by executing the Python file in a terminal or command prompt (e.g., python merge_pdfs.py).
A file dialog box will appear, allowing you to select the PDF files to be merged. Select one or more PDF files and click "Open".
The script will merge the selected PDF files and save the merged PDF document as "merged.pdf" in the same directory as the first selected PDF file.
The path to the saved merged PDF file will be printed to the console. A file dialogue box to the directory where the saved file is would open.

-------------------------------
License
-------------------------------
This script is released under the MIT License. Feel free to modify and use the script for your own purposes.
