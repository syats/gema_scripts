import csv

long_col="LON_DECIMAL"
lat_col= "LAT_DECIMAL"
mpo_col = "CVE_MUN"
edo_col = "CVE_ENT"
com_col = "CVE_LOC"

def MGEB_col2coords(filename):
    result = dict()
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            k = row[edo_col]+row[mpo_col]+row[com_col]
            v = (float(row[lat_col]),float(row[long_col]))
            result[k]=v
    return result