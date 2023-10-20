# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:34:24 2023

@author: Deperias Kerre
"""
from rdflib import Graph, RDF, RDFS, Literal, URIRef
from rdflib.namespace import FOAF, XSD
import pandas as pd
myGraph=Graph()
print(len(myGraph))
df=pd.read_csv("D:\ACADEMICS\PhD Computer Science\Research Work\QCL Project\QCL Ontology\TEST DATA\Data Analysis Trials\sample_data.csv")
print(df.head(3))
Dickson=URIRef("https://sces.strathmore.edu/faculty-profiles/dr-owuor-dickson-2/")
myGraph.add((Dickson, RDF.type, FOAF.Person))
myGraph.add((Dickson, FOAF.nick, Literal("Dickson", lang="en")))
Deperias=URIRef("https://www.linkedin.com/in/deperias-kerre-4b251ba9/")
myGraph.add((Deperias, RDF.type, FOAF.Person))
myGraph.add((Deperias, FOAF.nick, Literal("Deps", lang="en")))
#length
print(f"The graph has {len(myGraph)} elements")
for s,p,o in myGraph:
    print(s)