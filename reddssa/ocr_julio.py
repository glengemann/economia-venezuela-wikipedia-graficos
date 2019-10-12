# pip3 install pytesseract
# apt install tesseract-ocr-spa (3.04.00-1)
# apt install tesseract-ocr
# apt install gimagereader
from PIL import Image
import pytesseract
import re
import pandas as pd

image = '/home/prometeo/ProyectoGit/mercados-municipales/reddssa/15-26_july/monitoreo-de-precios-al-26-julio-2019-copia-4.png'

srt = pytesseract.image_to_string(
    Image.open(image),
    lang='spa'
)

srt = srt.replace(".","")
srt = srt.replace("'","")
srt = srt.replace("\n","")
srt = srt.replace("…","")

# pattern = re.compile(r'(\n[A-Z\s]*)\s*([0-9]*)\s*([0-9]*)')
pattern = re.compile(r'([A-Z1 ]*)(\s*[0-9]*)\s*([0-9]*)')
mach = pattern.findall(srt)

productos = []
for m in mach:
    if m[0] and m[1] and m[2]:
        productos.append(m)

df = pd.DataFrame(productos, columns=['Rubros','15 al 20 Jul','22 al 26 Ago'])
file_path = '/home/prometeo/ProyectoGit/mercados-municipales/reddssa/csv/'
df.to_csv(file_path + 'julio.csv', index=False)