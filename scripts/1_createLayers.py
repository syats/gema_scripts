import simplekml
import csv
import sys
from os.path import join as opj
from utils import MGEB_col2coords

data_folder = "./raw_data"
out_folder = "./results"
if len(sys.argv) > 1:
    data_folder = sys.argv[1]
if len(sys.argv) > 2:
    data_folder = sys.argv[2]

capas = [{"name": "planteles",
          "infile": opj(data_folder, "CATALOGO_CT.csv"),
          "com_col": "LOC",
          "edo_col": "ENT",
          "mpo_col": "MUN",
          "outfile": opj(out_folder, "planteles.kml"),
          "desc_col": "NOMBRECT",
          "id_col": "CLAVE_C"}]

# Cargar el marco geoestadístico
marco_geoestadistico = opj(data_folder, "marco.csv")

localidad2coordenas = MGEB_col2coords(filename=marco_geoestadistico)

found = 0
notfound = 0
for capa in capas:
    kml = simplekml.Kml()
    with open(capa["infile"], encoding="LATIN-1") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            description = row[capa["desc_col"]]
            com = row[capa["edo_col"]]+row[capa["mpo_col"]]+row[capa[
                "com_col"]]
            if len(com)==0:
                continue
            try:
                lat,long = localidad2coordenas[com]
                kml.newpoint(description=row[capa["desc_col"]],
                             coords=[(lat,long)])
                found += 1
            except:
                print(f"Coudn't find comunidad: {com}")
                notfound += 1
    kml.save(capa["outfile"])

    print(f"In total, found {found}, but missed {notfound}")
