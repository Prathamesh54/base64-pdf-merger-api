# 📄 Base64 PDF Merger API

A simple and robust REST API built using **FastAPI** that merges two PDF files sent as **Base64 encoded strings** and returns the merged PDF (also Base64 encoded).  
All PDF processing is done **100% in-memory** — no temporary files or disk usage.

This project was developed as a technical assignment.

---

## 🚀 Features

- Accepts two Base64 PDF inputs: `pdf1_base64` and `pdf2_base64`
- Validates Base64 input and PDF structure
- Decodes → Merges → Re-encodes entirely in memory
- Appends **PDF 2 after PDF 1**
- Returns the merged PDF as a Base64 string
- Handles:
  - Invalid Base64  
  - Corrupted PDF bytes  
  - Unexpected merge failures  
- Works with Swagger UI, Postman, and Python scripts

---

## 🛠️ Technologies Used

- **Python 3.12**
- **FastAPI**
- **pypdf**
- **uvicorn**

---

## 📡 API Endpoint

### **POST** `/merge-pdfs`

#### Request Body (JSON)
```json
{
  "pdf1_base64": "string",
  "pdf2_base64": "string"
}
```

#### Successful Response
```json
{
  "merged_pdf_base64": "string"
}
```

---

## ▶️ How to Run the API

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Prathamesh54/base64-pdf-merger-api.git
cd base64-pdf-merger-api
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start the API server
```bash
uvicorn app:app --reload --port 8000
```

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing the API

### ✔ Using Postman

POST → `http://127.0.0.1:8000/merge-pdfs`  
Body → Raw → JSON

```json
{
  "pdf1_base64": "BASE64_STRING",
  "pdf2_base64": "BASE64_STRING"
}
```

### ✔ Using Python scripts
```bash
python create_sample_pdfs.py
python test_merge.py
python test_merge_debug.py
```

Test output:
```
merged.pdf
```

---

## 📦 Project Structure

```
base64-pdf-merger-api/
│── app.py
│── requirements.txt
│── README.md
│── create_sample_pdfs.py
│── test_merge.py
│── test_merge_debug.py
│── write_b64_files.py
│── sample1.pdf
│── sample2.pdf
│── .gitignore
```

---

## ⚠️ Error Handling

| Code | Meaning                         |
|------|---------------------------------|
| 400  | Invalid Base64 or corrupted PDF |
| 500  | Unexpected merge error          |
| 200  | Success                         |

---


