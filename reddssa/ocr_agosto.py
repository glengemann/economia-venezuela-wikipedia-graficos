# pip3 install pytesseract
# apt install tesseract-ocr-spa (3.04.00-1)
# apt install tesseract-ocr
# apt install gimagereader
from PIL import Image
import pytesseract
import re
import pandas as pd

image = '/home/prometeo/ProyectoGit/mercados-municipales/reddssa/19-30_agosto/monitoreo-de-precios-al-30-agosto-4.png'

Image.open(image)

srt = pytesseract.image_to_string(
    Image.open(image),
    lang='spa'
)

srt = srt.replace(".","")
srt = srt.replace("'","")
srt = srt.replace("\n"," ")
srt = srt.replace("…","")

srt = "MONITOREO DE PRECIOS EN MERCADOS MUNICIPALES:, QUINTA CRESPO, CATIA, REPORTE DE PRECIOS C AR AC AS\n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\nQU ESO DURO 1KG 34.960 39.925\nLECHE EEGPOLVO 1 70.400 89.500\nMORTADELA 1KG 31.914 35.250\nPESCADO ATUN '\nFRESCO 56.214 34.800\nCURBINA 23.633 22.400\nSARDINA FRESCA 5.250 . 4.333\nPESCADO BONITA 23.133 21.875\nPESCADO\nRONCADOR 24.533 24.788\nPESCADO\nCOROCORO 23.740 ' 18.738\nPESCADO BAGRE 20.360 15.900\nPEPITONAS\nFRESCAS 16.069 21.125\nPESCADO BOCA\nCHICA 27.500 NO DISP\nPESCADO SALADO 35.800 ' 34.000\nHUEVOS 43.000 59.250\nCARNE DE CERDO 45.657 52.067\nCARNE DE RES 42.857 48.267\nPOLLO 30.357 33.575\nPECH UGA DE\nPOLLO 35.286 38.000\nMUSLO DE POLLO 33.950 38.000\n\n \n\n \n\nnº .\n\nBoiivanano\n\nAIin—ux-a'uu\n\n< Nutncion\n\nSAN MARTIN, GUAICAIPURO Y COCHE\n\nMARGEN DE AUMENTO DEL 19 DE AGOSTO AL 30 AGOSTO 2019\n\n38%\n\n27%\n14%\n\n10%\n\n-38%\n\nEl precio dela Leche en polvo de 1kg varía según su marca.\n\n \n\n…………..……… …"

srt = 'MONITOREO DE PRECIOS EN MERCADOS MUNICIPALES:, QUINTA CRESPO, CATIA, REPORTE DE PRECIOS C AR AC AS\n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\nQU ESO DURO 1KG 34.960 39.925\nLECHE EEGPOLVO 1 70.400 89.500\nMORTADELA 1KG 31.914 35.250\nPESCADO ATUN \nFRESCO 56.214 34.800\nCURBINA 23.633 22.400\nSARDINA FRESCA 5.250 . 4.333\nPESCADO BONITA 23.133 21.875\nPESCADO\nRONCADOR 24.533 24.788\nPESCADO\nCOROCORO 23.740  18.738\nPESCADO BAGRE 20.360 15.900\nPEPITONAS\nFRESCAS 16.069 21.125\nPESCADO BOCA\nCHICA 27.500 NO DISP\nPESCADO SALADO 35.800  34.000\nHUEVOS 43.000 59.250\nCARNE DE CERDO 45.657 52.067\nCARNE DE RES 42.857 48.267\nPOLLO 30.357 33.575\nPECH UGA DE\nPOLLO 35.286 38.000\nMUSLO DE POLLO 33.950 38.000\n\n \n\n \n\nnº .\n\nBoiivanano\n\nAIin—ux-auu\n\n< Nutncion\n\nSAN MARTIN, GUAICAIPURO Y COCHE\n\nMARGEN DE AUMENTO DEL 19 DE AGOSTO AL 30 AGOSTO 2019\n\n38%\n\n27%\n14%\n\n10%\n\n-38%\n\nEl precio dela Leche en polvo de 1kg varía según su marca.\n\n \n\n…………..……… …'


srt = 'QUESO DURO 1KG 34960 39925 LECHE EN POLVO 1KB 70400 89500'
pattern =  re.compile(r'[A-Z0-9]+')
pattern =  re.compile(r'[A-Z]+[0-9]?\s?')
pattern =  re.compile(r'([A-Z0-9]+\s?)\s([0-9\.]+)\s([0-9\.]+)')
pattern =  re.compile(r'(\w+){1,3}')
pattern.findall(srt)
it = pattern.finditer(srt)
match = it.__next__
dir(match)
next(it)
match = next(it)
match.groups()
match.span()

# pattern = re.compile(r'(\n[A-Z\s]*)\s*([0-9]*)\s*([0-9]*)')
pattern = re.compile(r'([A-Z1 ]*)(\s*[0-9]*)\s*([0-9]*)')
pattern.findall(srt)
mach = pattern.findall(srt)

productos = []
for m in mach:
    if m[0] and m[1] and m[2]:
        productos.append(m)

df = pd.DataFrame(productos, columns=['Rubros','19 al 23 Ago','26 al 30 Ago'])
file_path = '/home/prometeo/ProyectoGit/mercados-municipales/reddssa/csv/'
df.to_csv(file_path + 'agosto.csv', index=False)