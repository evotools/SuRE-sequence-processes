import pandas as pd

# Read input and params
data = pd.read_csv(snakemake.input.in_data)
l_f = snakemake.params.lf
r_f = snakemake.params.rf

# Vectorized operation (Faster and cleaner than row-iteration)
# 1. Calculate new columns
data["flank_start"] = data["start"] - l_f
data["flank_end"] = data["end"] + r_f

# 2. Create geneid

# 3. Rename/Select columns to match desired output
# Assuming the input has 'chrom', 'start', 'end', 'strand'
output_df = data[["chrom", "flank_start", "flank_end", "strand"]].copy()
output_df.columns = ["chrom", "flank_start", "flank_end", "flank_strand"]

# Save
output_df.to_csv(snakemake.output.out_data, index=False)