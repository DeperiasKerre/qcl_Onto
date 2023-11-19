### SPARQL Queries for Competency Questions

[SPARQL Documentation](https://www.w3.org/TR/rdf-sparql-query/).

CQ 1.1:  
CQ 1.2:


CQ 2.1:
```
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    PREFIX qudt:<http://qudt.org/schema/qudt/>
    SELECT ?HM ?seq ?unit ?ls
WHERE
{
 ?HM QpOnto:matFormula "GaAs/Al0.15Ga0.85As".
 ?ls QpOnto:basedOnMaterials ?HM;
  qudt:hasUnit ?unit; 
  QpOnto:sequence ?seq
}
```
