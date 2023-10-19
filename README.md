# Computational-Genomics

Computational Genomics involves the use of computational and statistical analysis to make interpretations from genome sequences and other data. 
It involves Genome Assembly, Gene Prediction, Functional Genomics, and Comparative Genomics.
There are numerous publicly available tools that can help with each of these steps. For the prokaryotic genomes, due to a multitude of options available, it can be daunting to choose the best tool for the user's dataset.
This repository provides codes for performing a comparison between popular tools based on various metrics and also provides a pipeline that can be implemented by the user for streamlining their analyses. 

**Gene Prediction**
Gene Prediction is the process of identifying regions that encode genes. There are two codes for this step in the repository:

1. Gene_prediction.py: Gene Prediction is a crucial step in Computational Genomics. This code takes the contigs .fasta files as input which can be generated performing Genome Assembly. The code uses 3 different gene prediction tools and compares their CPU Usage, RAM, and duration. The tools compared are:
   1. Prodigal:https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-119
   2. FragGeneScan: https://pubmed.ncbi.nlm.nih.gov/20805240/
   3. Balrog: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008727
  
2. gene_prediction_comparison.py: ORForise is a tool used for comparison of Gene Prediction results from two different tools. This code takes the following input:
gene prediction results files from Prodigal and FragGeneScan
It gives the following output: csv file containing the comparison of the tools based on various metrics.
Here is the link to GitHub of ORForise: https://github.com/NickJD/ORForise

**Comparative Genomics**
Comparative analysis is done to identify similarities and differences between genomes or genetic sequences, which can provide insights into the function, evolution, and relationships between the strains. 
This can aid in understanding genetic variation, gene function, and potential applications in fields the field of medicine. 

comparative_genomics_pipeline.py: This pipeline will utilize FastANI, SKANI, MLST, Parsnp, and Maast to perform whole genome, SNP, and accessory genome analyses on de novo assembled genomes or raw sequencing reads for outbreak analysis of bacterial genomes. 
