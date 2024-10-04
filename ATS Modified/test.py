import PyPDF2

with open(r"C:\Users\Virat\OneDrive\Desktop\ineni_Sreenivasarao_02092024.pdf", "rb") as pdf:
    reader= PyPDF2.PdfReader(pdf)
    print("number of pages", len(reader.pages))