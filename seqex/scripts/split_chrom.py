import pandas as pd

data = pd.read_csv(snakemake.input.dataset)
data['chrom'] = data["chrom"].astype(int)
chrom = int(snakemake.wildcards.chrom)

data_chr_df = data[data['chrom'] == chrom].reset_index(drop=True)
data_df = data_chr_df.drop_duplicates(subset=["chrom", "start", "end", "strand"]).reset_index(drop=True)

data_df.to_csv(snakemake.output.csv, index=False)