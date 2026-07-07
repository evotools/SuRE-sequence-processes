import pandas as pd
import sys

df = pd.read_csv(snakemake.input.csv)

bed_df = df.iloc[:, [0, 1, 2, 4, 5, 3]]
bed_df.to_csv(snakemake.output.bed, sep='\t', header=False, index=False)

# cols = [0, 1, 2, 4, 5, 3, 6, 7, 8, 9, 10, 11]
cols = [0, 1, 2, 4, 5, 3]
tmp_df = df.iloc[:, cols]
tmp_df.to_csv(snakemake.output.tmp, sep='\t', header=False, index=False)