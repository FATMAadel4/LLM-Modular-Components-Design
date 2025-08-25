from docx import Document
from pathlib import Path

def extract_text_from_docx(docx_path):
    try:
        # Open the Word document
        doc = Document(docx_path)
        full_text = []

        # Extract text from each paragraph
        for para in doc.paragraphs:
            full_text.append(para.text)

        return "\n".join(full_text)
    except Exception as e:
        return f"Error reading file: {e}"

def save_text_to_file(text, output_path):
    """Save extracted text to a file with UTF-8 encoding"""
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"✅ Text successfully saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

input_file = r"DataParsing_from_word/SampleFiles/arabic_text.docx"  # English, Arabic, or Mixed


doc_name = Path(input_file).stem
output_file = f"DataParsing_from_word/SampleOutput/{doc_name}_extracted.txt"

# Extract
text = extract_text_from_docx(input_file)

# Save
save_text_to_file(text, output_file)

print(f"Total characters extracted: {len(text)}")
