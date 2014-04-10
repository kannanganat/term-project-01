#!/usr/bin/env python

# please refer documentation of the project for details on the code. 


# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("Gene")

# Type constraints should come early - before all mentions of the paths they constrain
query.add_constraint("goAnnotation.ontologyTerm", "GOTerm")

# The view specifies the output columns
query.add_view(
    "symbol", "goAnnotation.ontologyTerm.name", "chromosomeLocation.start",
    "chromosomeLocation.end", "chromosome.primaryIdentifier",
    "interactions.details.experimentType", "interactions.gene2.symbol",
    "interactions.gene2.chromosome.primaryIdentifier",
    "interactions.gene2.chromosomeLocation.start",
    "interactions.gene2.chromosomeLocation.end"
)

# Uncomment and edit the line below (the default) to select a custom sort order:
# query.add_sort_order("Gene.symbol", "ASC")

# You can edit the constraint values below
query.add_constraint("goAnnotation.qualifier", "IS NULL", code = "C")
query.add_constraint("goAnnotation.qualifier", "!=", "NOT", code = "B")
query.add_constraint("goAnnotation.ontologyTerm.name", "CONTAINS", "cytoplasmic translation", code = "A")
query.add_constraint("name", "ONE OF", ["Ribosomal Protein of the Large subunit", "Ribosomal Protein of the Small subunit"], code = "D")

# Your custom constraint logic is specified with the code below:
query.set_logic("A and (B or C) and D")

for row in query.rows():
    print row["symbol"], row["goAnnotation.ontologyTerm.name"], row["chromosomeLocation.start"], \
        row["chromosomeLocation.end"], row["chromosome.primaryIdentifier"], \
        row["interactions.details.experimentType"], row["interactions.gene2.symbol"], \
        row["interactions.gene2.chromosome.primaryIdentifier"], \
        row["interactions.gene2.chromosomeLocation.start"], \
        row["interactions.gene2.chromosomeLocation.end"]

