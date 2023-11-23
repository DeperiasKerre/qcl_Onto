### Ontology Evaluation 
#### Consistency Check
The consistency check report from OOPS! Scanner can be accessed [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/Figures/OOPS_Report.png) or [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/OOPS_Scanner-Report.html).
#### SPARQL Queries for the Competency Questions

The SPARQL documentation can be found [here](https://www.w3.org/TR/rdf-sparql-query/).      
The competency questions can be found in a csv file [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/Evaluation/Competency_Questions.csv).   
The results of the queries below can be found in the notebook [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/Evaluation/sparql_queries.ipynb) and the comparison with the actual data values [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/Evaluation/query_results.csv).  
The query statistics can be obtained by the file [here](https://github.com/DeperiasKerre/qcl_Onto/blob/main/Evaluation/query_statistics.py).    
CQ 1.1: 
```
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    SELECT DISTINCT ?mat_composition
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:BoundToContinum;
     QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
}
```
CQ 1.2:
```
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
```
CQ 2.1:
```
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
```
CQ 3.1
```
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
```
CQ 3.2
```
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
```
CQ 4.1
```
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
```
CQ 4.2
```
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
```
CQ 5.1
```
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
```
CQ 5.2
```
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
```
CQ 5.3
```
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
```

