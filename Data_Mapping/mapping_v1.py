# -*- coding: utf-8 -*-
"""
Created on Tues Oct 24 16:23:24 2023

@author: Deperias Kerre
"""
#libraries
from rdflib import Graph, Literal, RDF, RDFS, URIRef
import pandas as pd

#import csv dataset
df=pd.read_csv("D:\ACADEMICS\PhD Computer Science\Research Work\QCL Project\QCL Ontology\TEST DATA\Data Analysis Trials\TEST_DATA.csv")

#view a section of data
df.head()

#create a graph and parse the ontology
g=Graph()
g.parse("D:\ACADEMICS\PhD Computer Science\Research Work\QCL Project\QCL Ontology\TEST DATA\Data Analysis Trials\qclonto.owl")

#parsing each column data into a python list
print("Parsing data columns to lists...")
url_list=df["Publication URL"].tolist()
doi_list=df["DOI"].tolist()
materials_list=df["Materials"].tolist()
layersequence_list=df["Layer Sequence"].tolist()
LSunit_list=df["LSUnit"].tolist()
designtype_list=df["Design Type"].tolist()
workingtemperaturecw_list=df["Working Temperature CW"].tolist()
WTCWunit_list=df["WTCWUnit"].tolist()
workingmodecw_list=df["Working Mode CW"].tolist()
workingtemperaturepulsemode_list=df["WT (Pulse Mode)"].tolist()
WTPMunit_list=df["WTPMUnit"].tolist()
workingmodepm_list=df["WorkingModepm"].tolist()
output_power_list=df["Power"].tolist()
powerunit_list=df["PowerUnit"].tolist()
frequency_list=df["Frequency"].tolist()
frequencyunit_list=df["FrequencyUnit"].tolist()
print("Successfully parsed to lists.")

#just to verify the content of the list
#for i in materials_list:
    #print(i)
    
#property names
working_tempcw="Working Temperature CW"
working_temppm="WT (Pulse Mode)"
power="Power"
frequency="Frequency"

#declaring the URis for instantiation
url=URIRef("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#URL")
doi=URIRef("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#DOI")
materials=URIRef("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#matFormula")
layerseq=URIRef("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#sequence")
units=URIRef("https://qudt.org/schema/qudt/unit")
designname=URIRef("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#DesignName")
values=URIRef("https://qudt.org/schema/qudt/numericValue")
workingmodename=URIRef("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#WorkingModeName")
propertyname=URIRef("https://w3id.org/mdo/core/PropertyName")

#mapping the lists as instances of the URIs
#URL
for i in range(len(url_list)):
    g.add((Literal(url_list[i]), RDF.type, url))
#DOI
for i in range(len(doi_list)):
    g.add((Literal(doi_list[i]), RDF.type, doi))
#Materials
for i in range(len(materials_list)):
    g.add((Literal(materials_list[i]), RDF.type, materials))
#sequence
for i in range(len(layersequence_list)):
    g.add((Literal(layersequence_list[i]), RDF.type, layerseq))
#layersequenceunit
for i in range(len(LSunit_list)):
    g.add((Literal(LSunit_list[i]), RDF.type, units))
#design name
for i in range(len(designtype_list)):
    g.add((Literal(designtype_list[i]), RDF.type, designname)) 
#working temperature cw values
for i in range(len(workingtemperaturecw_list)):
    g.add((Literal(workingtemperaturecw_list[i]), RDF.type, values))     
#working temperature cw units
for i in range(len(WTCWunit_list)):
    g.add((Literal(WTCWunit_list[i]), RDF.type, units))
#workingmode cw
for i in range(len(workingmodecw_list)):
    g.add((Literal(workingmodecw_list[i]), RDF.type, workingmodename))
#working temperature pm
for i in range(len(workingtemperaturepulsemode_list)):
    g.add((Literal(workingtemperaturepulsemode_list[i]), RDF.type, values))
#working temperature pm units
for i in range(len(WTPMunit_list)):
    g.add((Literal(WTPMunit_list[i]), RDF.type, units))
#working mode pm
for i in range(len(workingmodepm_list)):
    g.add((Literal(workingmodepm_list[i]), RDF.type, workingmodename))
#power values
for i in range(len(output_power_list)):
    g.add((Literal(output_power_list[i]), RDF.type, values))
#power units
for i in range(len(powerunit_list)):
    g.add((Literal(powerunit_list[i]), RDF.type, units))
#frequncy values
for i in range(len(frequency_list)):
    g.add((Literal(frequency_list[i]), RDF.type, values))
#frequency units
for i in range(len(frequencyunit_list)):
    g.add((Literal(frequencyunit_list[i]), RDF.type, units))
print("Mapping Succesful...")

#mapping the property names
g.add((Literal(working_tempcw), RDF.type, propertyname))
g.add((Literal(working_temppm), RDF.type, propertyname))
g.add((Literal(power), RDF.type, propertyname))
g.add((Literal(frequency), RDF.type, propertyname))
print("Mapping Succesful...")

#serialize into an rdf file in the current directory
g.serialize(destination="file.rdf")



