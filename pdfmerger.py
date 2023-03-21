import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfMerger

# Get the paths of the PDF files to be merged
Tk().withdraw()
pdf_files = askopenfilenames(filetypes=[('PDF Files', '*.pdf')])

# Merge the PDF files into a single PDF document
pdf_merger = PdfMerger()
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file:
        pdf_merger.append(file)

# Save the merged PDF document
merged_file_path = os.path.join(os.path.dirname(pdf_files[0]),'merged.pdf')
with open(merged_file_path, 'wb') as file:
    pdf_merger.write(file)
    print(f"Merged file saved to {merged_file_path}")
