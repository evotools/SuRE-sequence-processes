# SuRE sequence processes
The following repository contains all the codes regarding processing the TSS regions from a CSV file. Two distinct nextflow pipelines have been developed that can automatically extract sequences and the corresponding SuRE scores associated with those regions. The full pipeline would give out H5 files as output which can directly be used to train the models. 

## Table of contents
- [Processes](#processes)
- [Sub-processes](#sub-processes)
    - [posex](#posex)
    - [seqex]()
- [Usage]()
- [Modifications]()

## Processes
There are two processes that must be run to get the H5 files.
- `posex`: This contains the repository that will take the TSS regions as input and will give out the corresponding SuRE scores as output
- `seqex`: This contains the repository that will take the TSS regions (along with their corresponding scores) as input and give out the final H5 files that could be directly used for model training

## Sub-processes
### posex
Posex is a nextflow pipeline that takes the TSS regions as a CSV file and outputs the corresponding SuRE scores associated with that genomic region. The pipeline takes the following input:
- `dataset`: location of the CSV file
- `reads_directory`: location of the chromosome-separated reads directory (in BED format)
- `bw_file`: location of the bigwig file to know the legth of the chromosome
- `output_dir`: output directory
- `lf`: how much flanking sequence to take upstream of TSS (for our experiments, we had set this to 300)
- `rf`: how much flanking sequence to take downstream of TSS (for our experiments, we had set this to 300)
- `alpha`: To normalise the scores (when considering multiple animals)
- `epsilon`: added to deal with `log(0)` situations
- `cell_type`: cell type of interest
- `cell_sample`: cell sample of interest
- `stride`: Our methods create a stride to look at not only the TSS regions but also the surrounding regions that has helped in increasing the information content. This is a boolean to set whether strides should be extracted during this set or not
- `num_strides`: This number is being used to set how many strides should be used upstream/downstream of TSS
- `stride_length`: What should be the gap between each stride centre as compared to the TSS
- `chromosomes`: Which chromosomes is being preferred? Here, we have always pushed for chromosome-wise processing because this ensures parallelism

### seqex
Seqex is a nextflow pipeline that takes the TSS regions as a CSV files and outputs the corresponding sequences and converts them into H5 files that could be directly used for model training. The pipeline takes the following inputs:
- `dataset`: location of the CSV file
- `genome`: location of the genome FASTA file
- `output_dir`: output directory
- `chromosomes`: Which chromosomes is being preferred?

Please have a look at our paper[[1]](https://www.biorxiv.org/content/10.64898/2026.05.06.723179v1.full) to have a detailed understanding about the method.

## References
1. [Zhao R., Plenderleith L. J., Debnath T. et al. A high-resolution atlas of cattle regulatory variants and their cross-species activity in matched human cells](https://www.biorxiv.org/content/10.64898/2026.05.06.723179v1.full)

> [!WARNING]
>
> The following package of processes can not be directly used to create H5 files for model training. It has to be edited accordingly. Please see above regarding the modifications that has to be made. The following repository already has some test data files that could be used to test the proper functioning of the pipeline.