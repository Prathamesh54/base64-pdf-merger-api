import base64
import requests

def file_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

pdf1_b64 = file_to_b64("sample1.pdf")
pdf2_b64 = file_to_b64("sample2.pdf")

payload = {
    "pdf1_base64": pdf1_b64,
    "pdf2_base64": pdf2_b64
}

resp = requests.post("http://127.0.0.1:8000/merge-pdfs", json=payload)

print("STATUS:", resp.status_code)
print("RESPONSE BODY:")
print(resp.text)    # <-- this prints the JSON error message from the API

if resp.status_code == 200:
    merged_b64 = resp.json()["merged_pdf_base64"]
    with open("merged.pdf", "wb") as f:
        f.write(base64.b64decode(merged_b64))
    print("Merged PDF written to merged.pdf")
else:
    print("Merge failed. See the response above.")
