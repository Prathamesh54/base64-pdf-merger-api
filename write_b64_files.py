import base64

def write_b64(src, dest):
    with open(src, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    with open(dest, "w") as out:
        out.write(data)
    print(dest, "written (length:", len(data), ")")

write_b64("sample1.pdf", "b1.txt")
write_b64("sample2.pdf", "b2.txt")
