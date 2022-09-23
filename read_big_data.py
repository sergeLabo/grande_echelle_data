
import gzip

fichier = '/media/data/3D/projets/grande_echelle_data/MOBE_1/2022_06_08/cap_2022_06_08_17_20.zip'

with gzip.open(fichier, 'rb') as f:
    data = f.read()
print(data)
