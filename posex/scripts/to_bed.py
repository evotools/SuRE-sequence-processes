import pandas as pd

data = pd.read_csv(snakemake.input.in_data)

bed_data = data[["chrom", "flank_start", "flank_end", "flank_strand"]]

bed_data.to_csv(snakemake.output.out_data, sep='\t', header=None, index=None)