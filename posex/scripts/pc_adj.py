import pandas as pd
import numpy as np

def __pull_data__(data_rows, window_start, window_end, cell_sample):
    adj_count, adj_ipcr = 0, 0

    for k in range(0, len(data_rows)):
        strand_start, strand_end = data_rows["sure_start"][k], data_rows["sure_end"][k]
        start_diff = strand_start - window_start
        end_diff = strand_end - window_end
        strand_length = strand_end - strand_start

        if start_diff >= 0 and end_diff >= 0:
            contribution_length = window_end - strand_start
        elif start_diff < 0 and end_diff < 0:
            contribution_length = strand_end - window_start
        elif start_diff < 0 and end_diff >= 0:
            contribution_length = window_end - window_start
        elif start_diff >= 0 and end_diff < 0:
            contribution_length = strand_end - strand_start

        contribution_pc = (contribution_length / strand_length)
        adj_count += contribution_pc * data_rows[cell_sample][k]
        adj_ipcr += contribution_pc * data_rows["sure_ipcr"][k]
    
    return adj_count, adj_ipcr


data = pd.read_csv(snakemake.input.in_data, sep='\t', header=None)
data.columns = ["sure_chrom", "sure_start", "sure_end", "sure_strand", "sure_ipcr", "sure_boaec_d1", "sure_boaec_d2", "sure_haec_d1", "sure_haec_d2", "match_chrom", "match_start", "match_end", "match_strand", "match_bp"]

grouped = data.groupby(["match_chrom", "match_start", "match_end"])
unique_pairs = grouped.groups.keys()

cell_type = snakemake.params.cell_type
cell_sample = f"sure_{cell_type}_{snakemake.params.cell_sample}"
epsilon = snakemake.params.epsilon
alpha = snakemake.params.alpha
opposite_strand = snakemake.params.opposite_strand

final_dataset = []

for pairs in unique_pairs:
    extracted_rows = grouped.get_group(pairs).reset_index(drop=True)
    strand_1 = extracted_rows['match_strand'][0]
    extracted_rows_strand_1 = extracted_rows[extracted_rows['sure_strand'] == strand_1].reset_index(drop=True)

    window_start, window_end = pairs[1], pairs[2]

    adj_count, adj_ipcr = __pull_data__(extracted_rows, window_start, window_end, cell_sample)

    final_dataset.append(
        [pairs[0], pairs[1], pairs[2], strand_1, adj_count, adj_ipcr, (adj_count+epsilon) * alpha/(adj_ipcr+epsilon), np.log((adj_count+epsilon) * alpha/(adj_ipcr+epsilon))]
    )

    if opposite_strand:
        strand_2 = '-' if strand_1 == '+' else '+'
        extracted_rows_strand_2 = extracted_rows[extracted_rows['sure_strand'] == strand_2].reset_index(drop=True)

        adj_count, adj_ipcr = __pull_data__(extracted_rows_strand_2, window_start, window_end, cell_sample)

        final_dataset.append(
            [pairs[0], pairs[1], pairs[2], strand_2, adj_count, adj_ipcr, (adj_count+epsilon) * alpha/(adj_ipcr+epsilon), np.log((adj_count+epsilon) * alpha/(adj_ipcr+epsilon))]
        )

final_dataset_df = pd.DataFrame(final_dataset, columns=["match_chrom", "match_start", "match_end", "match_strand", "count", "ipcr", "adj_count", "adj_count_log"])

final_dataset_df.to_csv(snakemake.output.out_data, index=False)