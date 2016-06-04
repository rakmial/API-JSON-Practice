import os
import pprint
import csv

DATADIR = r"C:\Users\Bash\Desktop\Udacity\2_Data Analysis\P2\Beatles"
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    n = 0
    with open(datafile,'r') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data
