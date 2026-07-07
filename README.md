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
Posex is basically a nextflow pipeline that takes the TSS regions as a CSV file and outputs the corresponding SuRE scores associated with that genomic region. 

## References
- [1]: <https://www.biorxiv.org/content/10.64898/2026.05.06.723179v1.full> "A high-resolution atlas of cattle regulatory variants and their cross-species activity in matched human cells"


> [!WARNING]
>
> The following package of processes can not be directly used to create H5 files for model training. It has to be edited accordingly. Please see above regarding the modifications that has to be made. The following repository already has some test data files that could be used to test the proper functioning of the pipeline.