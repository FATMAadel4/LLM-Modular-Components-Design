import fitz
from pathlib import Path

def extract_text_by_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        # Get text as dictionary with block information
        text_dict = page.get_text("dict")

        for block in text_dict["blocks"]:
            if "lines" in block:  # Text block
                block_text = ""
                for line in block["lines"]:
                    line_text = ""
                    for span in line["spans"]:
                        line_text += span["text"]
                    block_text += line_text + " "
                full_text += block_text.strip() + "\n"

    doc.close()
    return full_text

def save_text_to_file(text, output_path):
    """Save extracted text to a file with UTF-8 encoding"""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Extract text
text = extract_text_by_blocks("SampleFiles/arabic_text.pdf")

# Create output filename based on input PDF
pdf_name = Path("SampleFiles/arabic_text.pdf").stem  # Gets filename without extension
output_file = f"SampleOutput/{pdf_name}_extracted.txt"

# Save to file
save_text_to_file(text, output_file)

print(f"\nTotal characters extracted: {len(text)}")