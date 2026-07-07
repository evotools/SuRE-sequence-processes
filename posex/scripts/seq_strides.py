import pandas as pd
import pyBigWig as pbg

# ====================
# PARAMS
# ====================
chrom = snakemake.wildcards.chrom
num_strides = snakemake.params.num_strides
stride_length = snakemake.params.stride_length

# ====================
# FILES
# ====================
bw_file = pbg.open(snakemake.input.bw_file)
assert bw_file.isBigWig() == True, "Not a true coverage file"

data = pd.read_csv(snakemake.input.in_data)
data = data.drop_duplicates(subset=['chrom', 'start', 'end', 'strand']).reset_index(drop=True)


# ====================
# MAIN
# ====================
chrom_length = bw_file.chroms(str(chrom)) if bw_file.chroms(str(chrom)) is not None else bw_file.chroms(f"chr{chrom}")

final_data = []

for _, row in data.iterrows():
    chrom, start, end, strand = row['chrom'], row['start'], row['end'], row['strand']
    for j in range(1, num_strides+1):
        stride_n_start, stride_n_end = start - j*stride_length, end - j*stride_length
        stride_p_start, stride_p_end = start + j*stride_length, end + j*stride_length
        if stride_n_start >= 0 and stride_n_end >= 0:
            final_data.append([
                chrom, stride_n_start, stride_n_end, strand
            ])
        if stride_p_start < chrom_length and stride_p_end < chrom_length:
            final_data.append([
                chrom, stride_p_start, stride_p_end, strand
            ])

final_data_df = pd.DataFrame(final_data)
final_data_df.columns = ['chrom', 'start', 'end', 'strand']
final_data_df.to_csv(snakemake.output.out_data, sep='\t', header=None, index=None)