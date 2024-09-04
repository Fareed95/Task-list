from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=10)  # Adjust margin as needed

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=8)

# Title
pdf.cell(200, 6, txt="To,", ln=True)
pdf.cell(200, 6, txt="The Municipal Commissioner,", ln=True)
pdf.cell(200, 6, txt="Municipal Corporation of Greater Mumbai,", ln=True)
pdf.cell(200, 6, txt="Chembur East,", ln=True)
pdf.cell(200, 6, txt="Mumbai, Maharashtra.", ln=True)

# Line break
pdf.ln(5)

# Body of the letter
letter_body = (
    "Subject: Request for Issuance of Birth Certificate\n\n"
    "Respected Sir/Madam,\n\n"
    "I, Mehirun Sayed, daughter of Mustafa Sayed and Sahib bi Khatun Mustafa Sayed, "
    "am writing to request the issuance of my birth certificate. I was born at BARC Colony, "
    "Anushakti Nagar, Godavari Building, Room No. 69, First Floor, 400094.  "
    "Currently, I reside at Room no. 89, Behind Building No.5, Subhash Nagar, Chembur, Mumbai, Maharashtra, 400071. "
    "After my marriage, I shifted to my present address. My husband's name is Khalil Sayed.\n"
    "In support of my request, I have attached the following documents:\n"
    "1. Living Certificate\n"
    "2. Death Certificate of my father, Mustafa Sayed\n"
    "3. My mother's Aadhar Card and CHS Card xerox\n\n"
    "The birth certificate is mandatory for updating my legal documents such as Aadhar, PAN card, and other related documents.\n"
    "I kindly request you to process my application at the earliest and provide me with my birth certificate."
    "Thank you for your attention to this matter.\n\n"
    "Yours faithfully,\n"
    "Mehirun Sayed\n"
    "Room no. 89, Behind Building No.5,\n"
    "Subhash Nagar, Chembur,\n"
    "Mumbai, Maharashtra, 400071\n"
    "Phone: 9136856391\n"
    "Email: mehirunsayed@gmail.com"
)

# Add the letter content
pdf.multi_cell(0, 6, letter_body)  # Adjust height parameter to minimize extra space

# Save the PDF to a file
pdf_file_path = 'C:\\Users\\Admin\\Documents\\Request_for_Birth_Certificate_Full_Letter_final.pdf'

pdf.output(pdf_file_path)

print(f"PDF saved to {pdf_file_path}")
