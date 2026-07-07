# seqEx: A sequence extraction method
This repository contains a snakemake pipeline to extract the FASTA sequences from a given genomic region, given the FASTA sequence file.

# Running the pipeline
Put the CSV file of the desired locations in the `data/` folder. Put the genome in the `genomes/` folder. Change the config file according to the needs.

To run the pipeline, use the following command:
```
snakemake --cores 1
```

We have used one core to make the pipeline easy to implement but that can be changed based on the requirements of the user