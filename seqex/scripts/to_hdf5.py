import pandas as pd
import h5py
import numpy as np

tsv_df = pd.read_csv(snakemake.input.tsv, sep='\t', header=None)
output_path = snakemake.output.h5

chroms = tsv_df[0].values.astype('S')
starts = tsv_df[1].values.astype(np.int64)
ends = tsv_df[2].values.astype(np.int64)
strands = tsv_df[5].values.astype('S') # Assuming strand is col 5
# cdna_counts = tsv_df[4].values.astype(np.float32) # Assuming score/cdna is col 4
sequences = tsv_df.iloc[:, -1].values.astype('S') # Last column is sequence

# GeneID format: chrom_start_end_strand
names = (tsv_df[0].astype(str) + "_" + tsv_df[1].astype(str) + "_" + 
            tsv_df[2].astype(str) + "_" + tsv_df[5].astype(str)).values.astype('S')

with h5py.File(output_path, 'w') as hf:
    hf.create_dataset('chrom', data=chroms)
    hf.create_dataset('start', data=starts)
    hf.create_dataset('end', data=ends)
    hf.create_dataset('strand', data=strands)
    # hf.create_dataset('cDNA_count', data=cdna_counts)
    hf.create_dataset('sequence', data=sequences)
    hf.create_dataset('geneid', data=names)