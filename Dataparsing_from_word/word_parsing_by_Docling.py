from docling.document_converter import DocumentConverter
import os

# Input / Output paths
input_file = "DataParsing_from_word/SampleFiles/arabic_text.docx"
output_file = "DataParsing_from_word/SampleOutput/arabic_text_extracted.txt"

# Ensure output folder exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Initialize Docling converter
converter = DocumentConverter()

# Convert (returns ConversionResult)
result = converter.convert(input_file)

# Get the actual document object
doc = result.document

# Extract plain text

#text = doc.export_to_text()   
        

# Save extracted text to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(doc)

print(f" Extracted text saved to {output_file}")
