# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:38:04 2023

@author: Deperias Kerre
"""
#import libraries
import pandas as pd
from rdflib import Graph, Literal, RDF, RDFS, URIRef, OWL
#import the dataset
df=pd.read_csv("C:/Users/USER/Documents/Projects/TEST_DATA.csv")
#parsing the ontology into an rdf graph
myGraph=Graph()
myGraph.parse("C:/Users/USER/Documents/Projects/qclonto.owl")
#URIS
#QCL Ontology namespace prefix
QpOnto="https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#"
##Ontology Classes/Concepts
qcl=URIRef(QpOnto+"QuantumCascadeLaser")
heterostructure=URIRef(QpOnto+"LaserHeterostructure")
working_mode=URIRef(QpOnto+"LaserWorkingMode")
materials=URIRef(QpOnto+"HeterostructureMaterials")
layer_sequence=URIRef(QpOnto+"LayerSequence")
unit=URIRef("https://qudt.org/schema/qudt/Unit")
quantity_value=URIRef("http://qudt.org/schema/qudt/QuantityValue")
quantity_kind=URIRef("https://qudt.org/schema/qudt/QuantityKind")
laser_design=URIRef(QpOnto+"LaserDesignType")
academic_article=URIRef("http://purl.org/ontology/bibo/AcademicArticle")
Property=URIRef("https://w3id.org/mdo/core/Property")
# URIs for Instances
##Quantity Values
power_value=URIRef(QpOnto+"PowerValue")
temp_value=URIRef(QpOnto+"WorkingTempValue")
frequency_value=URIRef(QpOnto+"FrequencyValue")
##Laser Working Modes
continous_wave=URIRef(QpOnto+"ContinousWaveOperation")
pulsed_mode=URIRef(QpOnto+"PulsedOperation")
##Laser Optoelectronic Properties
working_temperature=URIRef(QpOnto+"WorkingTemperature")
optical_power=URIRef(QpOnto+"OpticalPower")
lasing_frequency=URIRef(QpOnto+"LasingFrequency")
##Laser Design Types
lo_phonon=URIRef(QpOnto+"LOPhononDepopulation")
bound_continum=URIRef(QpOnto+"BoundToContinum")
double_resonant=URIRef(QpOnto+"DoubleResonantPhonon")
#object properties 
has_property=URIRef(QpOnto+"hasProperty")
has_quantitykind=URIRef("https://qudt.org/schema/qudt/hasQuantityKind")
attributed_to=URIRef("http://www.w3.org/ns/prov#wasAttributedTo")
has_heterostructure=URIRef(QpOnto+"hasHeterostructure")
has_materials=URIRef(QpOnto+"hasMaterials")
has_designtype=URIRef(QpOnto+"hasDesignType")
has_layersequence=URIRef(QpOnto+"hasLayerSequence")
based_on_materials=URIRef(QpOnto+"basedOnMaterials")
relates_to_heterostructure=URIRef(QpOnto+"relatesToHeterostructure")
corresponds_to_working_mode=URIRef(QpOnto+"correspondsToWorkingMode")
has_unit=URIRef("https://qudt.org/schema/qudt/hasUnit")
has_working_mode=URIRef(QpOnto+"hasWorkingMode")
has_quantity_value=URIRef("https://qudt.org/schema/qudt#hasQuantityValue")
#URIs for optolectronic Property Units
qudt_unit="https://qudt.org/vocab/unit/"
Kelvin=URIRef(qudt_unit+"K")
Milliwatt=URIRef(qudt_unit+"MilliW")
TeraHertz=URIRef(qudt_unit+"TeraHZ")
Nanometer=URIRef(qudt_unit+"NanoM")
Angstrom=URIRef(qudt_unit+"ANGSTROM")
#URIs for Quantity Kinds
qudt_quantitykind="https://qudt.org/vocab/quantitykind/"
power=URIRef(qudt_quantitykind+"Power")
frequency=URIRef(qudt_quantitykind+"Frequency")
temperature=URIRef(qudt_quantitykind+"Temperature")
#URIs for data properties
doi_prop=URIRef(QpOnto+"DOI")
materials_prop=URIRef(QpOnto+"matFormula")
layerseq_prop=URIRef(QpOnto+"sequence")
numerical_value=URIRef("https://qudt.org/schema/qudt/numericValue")
publication_url=URIRef(QpOnto+"URL")
#data enrichment with uris for the qcl, heterostructure, material, layer sequence, designtype and units.
df["QID"]=df["QID"].apply(lambda q : QpOnto + q)
df["HSID"]=df["HSID"].apply(lambda q : QpOnto + q)
df["MatID"]=df["MatID"].apply(lambda q : QpOnto + q)
df["LSID"]=df["LSID"].apply(lambda q : QpOnto + q)
df["LSUnit"]=df["LSUnit"].apply(lambda q : Angstrom if q=="Å" else Nanometer )
df["WTCWUnit"]=df["WTCWUnit"].apply(lambda q : Kelvin if q=="K" else "none")
df["WorkingModeCW"]=df["WorkingModeCW"].apply(lambda q : continous_wave if q=="Continous Wave" else "none")
df["WTPMUnit"]=df["WTPMUnit"].apply(lambda q : Kelvin if q=="K" else "none")
df["WorkingModepm"]=df["WorkingModepm"].apply(lambda q : pulsed_mode if q=="Pulse Mode" else "none")
df["PowerUnit"]=df["PowerUnit"].apply(lambda q : Milliwatt if q=="mW" else "none")
df["FrequencyUnit"]=df["FrequencyUnit"].apply(lambda q : TeraHertz if q=="THz" else "none")
df["WTCWVID"]=df["WTCWVID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["WTPMVID"]=df["WTPMVID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["PVID"]=df["PVID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["FVID"]=df["FVID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["WTCWPID"]=df["WTCWPID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["WTPMPID"]=df["WTPMPID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["PPID"]=df["PPID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
df["FPID"]=df["FPID"].apply(lambda q : "none" if q=="none" else QpOnto + q)
#enrichig with the design type URIs
def designtype_mapper(a):
    if a=="LOphonon":
        return lo_phonon
    elif a=="Resonantphonon":
        return double_resonant
    elif a=="boundtocontinum":
        return bound_continum
    else:
        return "none"
df["DesignType"]=df["DesignType"].apply(lambda q : designtype_mapper(q))
#Data mapping
##mapping instances
##qcl id, publication url, hsid, matid, lsid 
for a,b,c,d,e in zip (df["QID"],df["PublicationURL"],df["HSID"],df["MatID"],df["LSID"]):
    myGraph.add((URIRef(a), RDF.type, (qcl)))
    myGraph.add((URIRef(b), RDF.type, (academic_article)))
    myGraph.add((URIRef(c), RDF.type, (heterostructure)))
    myGraph.add((URIRef(d), RDF.type, (materials)))
    myGraph.add((URIRef(e), RDF.type, (layer_sequence)))  
##lsunit, wtcwunit, wtpmunit, power unit, frequency unit
for a,b in zip(df["LSUnit"],df["WTCWUnit"]):
    if("none" not in b):
        myGraph.add((URIRef(a), RDF.type, (unit)))
        myGraph.add((URIRef(b), RDF.type, (unit)))
for a in zip (df["WTPMUnit"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (unit)))
for a in zip(df["PowerUnit"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (unit)))
for a in zip(df["FrequencyUnit"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (unit)))
##quantity kinds
myGraph.add(((power), RDF.type, (quantity_kind)))
myGraph.add(((frequency), RDF.type, (quantity_kind)))
myGraph.add(((temperature), RDF.type, (quantity_kind)))
##quanity values
for a in zip(df["WTCWVID"]):
     if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (temp_value)))
for a in zip(df["WTPMVID"]):
     if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (temp_value)))
for a in zip(df["PVID"]):
     if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (power_value)))
for a in zip(df["FVID"]):
     if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (frequency_value)))
## property
for a in zip(df["WTCWPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (working_temperature)))
for a in zip(df["WTPMPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (working_temperature)))      
for a in zip(df["PPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (optical_power))) 
for a in zip(df["FPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), RDF.type, (lasing_frequency))) 
##mapping object properties between instances: 
###has property, was attributed to, has heterostructure, has working mode
for a,b,c in zip (df["QID"], df["HSID"], df["PublicationURL"]):
    myGraph.add((URIRef(a), has_heterostructure, URIRef(b)))
    myGraph.add((URIRef(a), attributed_to, URIRef(c)))
for a,b in zip(df["QID"],df["WorkingModeCW"]):
     if("none" not in b):
             myGraph.add((URIRef(a), has_working_mode, URIRef(b)))
for a,b in zip(df["QID"],df["WorkingModepm"]):
     if("none" not in b):
             myGraph.add((URIRef(a), has_working_mode, URIRef(b)))            
for a,b in zip(df["QID"],df["WTCWPID"]):
     if("none" not in b):
             myGraph.add((URIRef(a), has_property, URIRef(b)))   
for a,b in zip(df["QID"],df["WTPMPID"]):
     if("none" not in b):
             myGraph.add((URIRef(a), has_property, URIRef(b)))                   
for a,b in zip(df["QID"],df["PPID"]):
     if("none" not in b):
             myGraph.add((URIRef(a), has_property, URIRef(b))) 
for a,b in zip(df["QID"],df["FPID"]):
     if("none" not in b):
             myGraph.add((URIRef(a), has_property, URIRef(b)))
###has design type, has materials,has layer sequence,  based on materials, has unit, relates to heterostructure
for a,b,c,d,e in zip(df["HSID"],df["DesignType"],df["LSID"],df["MatID"],df["LSUnit"]):
    if ("none" not in b):
        myGraph.add((URIRef(a), has_designtype, URIRef(b)))
        myGraph.add((URIRef(a), has_materials, URIRef(d)))
        myGraph.add((URIRef(a), has_layersequence, URIRef(c)))
        myGraph.add((URIRef(c), based_on_materials, URIRef(d)))
        myGraph.add((URIRef(c), has_unit, URIRef(e)))
### relates to heterostructure
for a,b in zip(df["WTCWPID"],df["HSID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), relates_to_heterostructure, URIRef(b)))
for a,b in zip(df["WTPMPID"],df["HSID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), relates_to_heterostructure, URIRef(b)))  
for a,b in zip(df["PPID"],df["HSID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), relates_to_heterostructure, URIRef(b)))
for a,b in zip(df["FPID"],df["HSID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), relates_to_heterostructure, URIRef(b)))
#has unit for quantity values
for a in (df["WTCWVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a),  has_unit, (Kelvin)))
for a in (df["WTPMVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a),  has_unit, (Kelvin)))
for a in (df["PVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a),  has_unit, (Milliwatt)))
for a in (df["FVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a),  has_unit, (TeraHertz)))
#has quantity kind, has quantity value, corresponds to working mode
for a in (df["WTCWPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantitykind, (temperature)))
for a in (df["WTPMPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantitykind, (temperature)))
for a in (df["PPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantitykind, (power)))
for a in (df["FPID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantitykind, (frequency)))
for a,b in zip(df["WTCWPID"],df["WTCWVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantity_value, URIRef(b)))
for a,b in zip(df["WTPMPID"],df["WTPMVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantity_value, URIRef(b)))
for a,b in zip(df["PPID"],df["PVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantity_value, URIRef(b)))
for a,b in zip(df["FPID"],df["FVID"]):
    if("none" not in a):
        myGraph.add((URIRef(a), has_quantity_value, URIRef(b)))
for a in (df["WTCWPID"]):
    if ("none" not in a):
         myGraph.add((URIRef(a), corresponds_to_working_mode, (continous_wave)))
for a in (df["WTPMPID"]):
    if ("none" not in a):
         myGraph.add((URIRef(a), corresponds_to_working_mode, (pulsed_mode)))
##populating the graph dataset with data literals using data properties
#populating doi, materials formula and the layer sequence
for a,b,c,d,e,f in zip(df["PublicationURL"],df["MatID"],df["LSID"],df["DOI"],df["Materials"],df["LayerSequence"]):
    myGraph.add((URIRef(a), doi_prop, Literal(d)))
    myGraph.add((URIRef(b), materials_prop, Literal(e)))
    myGraph.add((URIRef(c), layerseq_prop, Literal(f)))
    myGraph.add((URIRef(a), publication_url, Literal(a)))
#populating numerical values for power, frequency and temperature
for a,b in zip(df["WTCWVID"],df["WorkingTemperatureCW"]):
    if("none" not in a):
        myGraph.add((URIRef(a), numerical_value, Literal(b)))
for a,b in zip(df["WTPMVID"],df["WTPulseMode"]):
    if("none" not in a):
        myGraph.add((URIRef(a), numerical_value, Literal(b)))        
for a,b in zip(df["PVID"],df["Power"]):
    if("none" not in a):
         myGraph.add((URIRef(a), numerical_value, Literal(b)))
for a,b in zip(df["FVID"],df["Frequency"]):
    if("none" not in a):
         myGraph.add((URIRef(a), numerical_value, Literal(b))) 
#Generating the rdf graph dataset file in turtle format
myGraph.serialize(destination="data_file.ttl")        