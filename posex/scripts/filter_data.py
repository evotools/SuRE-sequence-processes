import pandas as pd
import numpy as np

data = pd.read_csv(snakemake.input.in_data)

data = data.drop_duplicates(subset=["match_chrom", "match_start", "match_end"]).reset_index(drop=True)

mean = np.mean(data['ipcr'])
std = np.std(data['ipcr'])

filtered_data = data[(data['ipcr'] >= mean - 2 * std) & (data['ipcr'] <= mean + 2 * std)].reset_index(drop=True)

filtered_data = filtered_data[["match_chrom", "match_start", "match_end", "match_strand", "adj_count", "adj_count_log"]]

filtered_data.columns = ["chrom", "start", "end", "strand", "adj_count", "adj_count_log"]

filtered_data.to_csv(snakemake.output.out_data, index=False)