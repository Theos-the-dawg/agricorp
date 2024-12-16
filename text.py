from docx import Document

# Load the provided document
file_path = "/mnt/data/AGREEMENT FEES.docx"
doc = Document(file_path)

# Format improvements
# Define header and footer content
header_text = "ATTORNEYS, NOTARIES, CONVEYANCERS & ESTATE PLANNERS\n" \
              "Mbalisto House, 17 Brander Street, Mbombela 1200\n" \
              "Tel: (013) 752 6936 | Fax: (013) 753 2278 | P.O BOX 894, MBOMBELA, 1200\n" \
              "E-mail: virginia@nsalaw.co.za, nomaswazi@nsalaw.co.za | VAT 4650260377"

footer_text = "Confidential Legal Document | Prepared by Nomaswazi Shabangu Attorneys"

# Create a new document for better structure
new_doc = Document()

# Add formatted header
new_doc.add_paragraph(header_text).alignment = 1  # Center alignment

# Process the content and structure it
for para in doc.paragraphs:
    # Skip excessive whitespace and redundant information
    if para.text.strip():
        # Add titles and main sections as bold headings
        if para.text.upper() == para.text:
            new_doc.add_paragraph(para.text, style="Heading 1")
        else:
            new_doc.add_paragraph(para.text)

# Add footer
footer_section = new_doc.sections[-1]
footer = footer_section.footer
footer.paragraphs[0].text = footer_text
footer.paragraphs[0].alignment = 1  # Center alignment

# Save the formatted document
formatted_file_path = "/mnt/data/Formatted_AGREEMENT_FEES.docx"
new_doc.save(formatted_file_path)

formatted_file_path
