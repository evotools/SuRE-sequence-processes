import pandas as pd

filtered_data = pd.read_csv(snakemake.input.filtered_data)
all_data = pd.read_csv(snakemake.input.all_data)

all_data.columns = ['chrom', 'start', 'end', 'strand', 'count', 'ipcr', 'adj_count', 'adj_count_log']

data = all_data.merge(
    filtered_data,
    on=['chrom', 'start', 'end'],
    suffixes=['_all', '_filter']
)

data = data.dropna().reset_index(drop=True)

data = data[["chrom", "start", "end", "strand_all", "adj_count_all", "adj_count_log_all"]]
data.columns = ["chrom", "start", "end", "strand", "adj_count", "adj_count_log"]

data.to_csv(snakemake.output.out_data, index=None)