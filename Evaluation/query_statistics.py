# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:21:48 2023

@author: Deperias Kerre
"""
#import graph
from rdflib import Graph
#create an rdf graph and parse the turtle file of the graph dataset
qpGraph=Graph()
file_path="C:/Users/USER/Documents/Projects/data_file.ttl"
qpGraph.parse(file_path)
#Query records statistics
#query 1.1
q1 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    SELECT DISTINCT ?mat_composition
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:BoundToContinum;
     QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
}
"""
a=0
for r in qpGraph.query(q1):
    a+=len(r)
#query 1.2
q2 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT ?seq ?unit
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:LOPhononDepopulation;
 QpOnto:hasLayerSequence ?ls.
 ?ls QpOnto:sequence ?seq;
  qudt:hasUnit ?unit 
}
"""
b=0
for r in qpGraph.query(q2):
    b+=len(r)
#query 2.1
q3 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    SELECT DISTINCT ?design_type
WHERE
{
 ?HS QpOnto:hasDesignType ?design_type;
 QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula "GaAs/Al0.15Ga0.85As".
}
"""
c=0
for r in qpGraph.query(q3):
    c+=len(r)
#query 3.1
q4 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT ?seq ?unit
WHERE
{
 ?HM QpOnto:matFormula "GaAs/Al0.15Ga0.85As".
 ?ls QpOnto:basedOnMaterials ?HM;
  qudt:hasUnit ?unit; 
  QpOnto:sequence ?seq
}
"""
d=0
for r in qpGraph.query(q4):
    d+=len(r)
#Question 4.1
q5 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT ?value ?unit 
WHERE
{
 ?wt QpOnto:correspondsToWorkingMode QpOnto:ContinousWaveOperation;
 <https://qudt.org/schema/qudt#hasQuantityValue> ?qv.
 ?qv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
}
"""
e=0
for r in qpGraph.query(q5):
    e+=len(r)
#question 4.2
q6 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT ?value ?unit 
WHERE
{
 ?wt QpOnto:correspondsToWorkingMode QpOnto:PulsedOperation;
 <https://qudt.org/schema/qudt#hasQuantityValue> ?qv.
 ?qv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
}
"""
f=0
for r in qpGraph.query(q6):
    f+=len(r)
#question 5.1 
q7 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT DISTINCT ?value ?unit
WHERE
{
 ?HM QpOnto:matFormula "GaAs/Al0.15Ga0.85As".
 ?HS QpOnto:hasMaterials ?HM.
?lf QpOnto:relatesToHeterostructure ?HS;
<https://qudt.org/schema/qudt#hasQuantityValue> ?qv.
 ?qv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 FILTER(?unit=<https://qudt.org/vocab/unit/TeraHZ>).
}
"""
g=0
for r in qpGraph.query(q7):
    g+=len(r)
#question 5.2
q8 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT ?value ?unit
WHERE
{
 ?HS QpOnto:hasLayerSequence ?ls.
 ?ls QpOnto:sequence "54/78/24/64/38/148/24/94";
 qudt:hasUnit <https://qudt.org/vocab/unit/ANGSTROM>.
 ?op QpOnto:relatesToHeterostructure ?HS;
 <https://qudt.org/schema/qudt#hasQuantityValue> ?qv.
 ?qv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 FILTER(?unit=<https://qudt.org/vocab/unit/MilliW>).
}
"""
h=0
for r in qpGraph.query(q8):
    h+=len(r)
#question 6.1
q9 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    SELECT DISTINCT ?mat_composition
WHERE
{
 ?lf <https://qudt.org/schema/qudt#hasQuantityValue> ?fv;
 QpOnto:relatesToHeterostructure ?HS.
 ?fv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?HS QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
 FILTER(?unit=<https://qudt.org/vocab/unit/TeraHZ>&&?value>3).
}
"""
i=0
for r in qpGraph.query(q9):
    i+=len(r)
#question 7.1
q10 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?qcl QpOnto:hasProperty ?wt;
prov:wasAttributedTo ?article.
?wt <https://qudt.org/schema/qudt#hasQuantityValue> ?qv;
QpOnto:correspondsToWorkingMode QpOnto:ContinousWaveOperation.
?qv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/K>&&?value>40).
}
"""
j=0
for r in qpGraph.query(q10):
    j+=len(r)
#question 7.2
q11 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?qcl QpOnto:hasHeterostructure ?HS;
prov:wasAttributedTo ?article.
?HS QpOnto:hasMaterials ?HM.
?HM QpOnto:matFormula "GaAs/Al0.15Ga0.85As".
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
}
"""
k=0
for r in qpGraph.query(q11):
    k+=len(r)
#question 7.3
q12 = """
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?qcl QpOnto:hasHeterostructure ?HS;
prov:wasAttributedTo ?article.
?HS QpOnto:hasDesignType QpOnto:LOPhononDepopulation.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
}
"""
l=0
for r in qpGraph.query(q12):
    l+=len(r)
#summary
print("***Summary for the Records Returned by the Queries***")
print("Records for queries for CQ1:")
print("CQ1.1", "number of records:", a,",", "CQ1.2", "number of records:", b)
print("Records for queries for CQ2:")
print("CQ2.1", "number of records:", c)
print("Records for queries for CQ3:")
print("CQ3.1", "number of records:", d)
print("Records for queries for CQ4:")
print("CQ4.1", "number of records:", e,",", "CQ4.2", "number of records:", f)
print("Records for queries for CQ5:")
print("CQ5.1", "number of records:", g,",", "CQ5.2", "number of records:", h)
print("Records for queries for CQ6:")
print("CQ6.1", "number of records:", i)
print("Records for queries for CQ7:")
print("CQ7.1", "number of records:", j, "CQ7.2", "number of records:", k, "CQ7.3", "number of records:", l)
print("Total records:", a+b+c+d+e+f+g+h+i+j+k+l)
print("**End of Report**")
