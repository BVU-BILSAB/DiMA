# What is DiMA?

Protein sequence diversity is one of the major challenges in the design of diagnostic, prophylactic and therapeutic 
interventions against viruses. DiMA is a tool designed to facilitate the dissection of protein sequence diversity 
dynamics for viruses.

DiMA provides a quantitative measure of sequence diversity by use of Shannon’s entropy, 
applied via a user-defined k-mer sliding window. Further, the entropy value is corrected for sample size bias by 
applying a statistical adjustment. 

DiMA further interrogates the diversity by dissecting the entropy value at each k-mer position to various 
diversity motifs. The distinct k-mer sequences at each position are classified into the following motifs based on 
their incidence. Index is the predominant sequence, and all other distinct k-mers are referred to as total variants, 
sub-classified into major variant (the predominant variant), minor variants (k-mers with incidence in between major 
and unique motifs) and unique variants (seen once in the alignment).

The description line of the sequences in the alignment can be formatted for inclusion of meta-data that can 
be tagged to the diversity motifs. 

DiMA enables comparative diversity dynamics analysis, within and between proteins of a virus species, and proteomes of 
different viral species.