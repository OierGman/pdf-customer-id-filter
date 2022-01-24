import requests
import pdfplumber
import re

pdfFile = ("C:\\Users\\oier-\\Desktop\\test document pdf reader.pdf")

with pdfplumber.open(pdfFile) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

print(text)

newReference = re.compile(r'Customer Reference ID :')

for line in text.split('\n'):
    if newReference.match(line):
        print("Result:")
        print(line)