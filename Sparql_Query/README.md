### SPARQL Queries for Competency Questions

[SPARQL Documentation](https://www.w3.org/TR/rdf-sparql-query/).

The results of the queries below can be found in the notebook [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/Sparql_Query/sparql_queriesv2.ipynb).     
CQ 1.1: 
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    SELECT ?HS ?HM ?mat_composition
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:BoundToContinum.
 ?HS QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
}
```
CQ 1.2:
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<http://qudt.org/schema/qudt/>
    SELECT ?HS ?ls ?seq ?unit
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:LOPhononDepopulation;
 QpOnto:hasLayerSequence ?ls.
 ?ls QpOnto:sequence ?seq;
  qudt:hasUnit ?unit 
}
```
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
CQ 3.1
