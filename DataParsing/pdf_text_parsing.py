import fitz

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


text = extract_text_by_blocks("mixed.pdf")
print(text)
