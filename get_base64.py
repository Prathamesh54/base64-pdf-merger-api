import base64

def encode(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

print("PDF1 Base64:")
print(encode("sample1.pdf"))
print("\n\nPDF2 Base64:")
print(encode("sample2.pdf"))
