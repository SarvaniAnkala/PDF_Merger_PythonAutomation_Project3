import PyPDF2
import os
import sys

# Create an instance of PdfMerger
merger = PyPDF2.PdfMerger()

# Loop through all files in the current directory
for file in os.listdir(os.curdir):
    # Check if the file is a PDF
    if file.endswith(".pdf"):
        # Append the PDF file to the merger
        merger.append(file)

# Write the combined PDF to a new file
merger.write("combinedBSUniDocs.pdf")

# Close the merger
merger.close()
