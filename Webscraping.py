import pandas as pd 
import os 
import requests
from Bio import Entrez
import xml.etree.ElementTree as ET
os.chdir("")

df = pd.read_csv("")


#### trying to webscraping

###### IT WORKS
Entrez.email="felipeschoninger@gmail.com"
def get_ncbi_gene_id(ensembl_id):

    handle= Entrez.esearch(db="gene" , term = ensembl_id)
    rec_list=Entrez.read(handle)
    handle.close()
    if "IdList" in rec_list and rec_list["IdList"]:
        return str(rec_list["IdList"][0])
    else:
        return "NCBI Gene ID not found"   

def get_ncbi_gene_description(NCBI_ID):
    if len(NCBI_ID) != 9:
        return "NCBI Gene description not found" 
    else:
        handle= Entrez.efetch(db="gene", id=NCBI_ID, rettype="gb")
        recs = handle.read()
        handle.close()
        root = ET.fromstring(recs)
        description = root.find(".//p[@class='desc']").text
        return description
           



df["NCBI_ID"] = df["Row.names"].apply(get_ncbi_gene_id)

df["description"] = df["description"].mask(df["description"].isna(), df["NCBI_ID"].apply(get_ncbi_gene_description))

df.to_csv("24VScontrolCOMPLETE.csv", index=False)
