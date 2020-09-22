import pdftotext

# Load your PDF
with open("sample.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
for page in pdf:
    print(page)
