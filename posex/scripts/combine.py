import pandas as pd

data_1 = pd.read_csv(snakemake.input.in_data_1)
data_2 = pd.read_csv(snakemake.input.in_data_2)
data_2 = data_2[["match_chrom", "match_start", "match_end", "match_strand", "adj_count", "adj_count_log"]]
data_2.columns = ["chrom", "start", "end", "strand", "adj_count", "adj_count_log"]

data = pd.concat(
    [data_1, data_2]
)

data.to_csv(snakemake.output.out_data, index=None)