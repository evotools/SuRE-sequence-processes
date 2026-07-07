import pandas as pd

# 1. Read the Metadata (BED tmp file)
# No header in file, so we assign generic names or indices
meta = pd.read_csv(snakemake.input.meta, sep='\t', header=None)

# 2. Read the Sequences (bedtools output)
# Format: "chr:start-end(strand)" <tab> "SEQUENCE"
seqs = pd.read_csv(snakemake.input.fasta, sep='\t', header=None, names=['location_id', 'sequence'])

# 3. Create a merge key in the Metadata
# Your awk script matched: chr:start-end(strand)
# Assuming meta columns: 0=chr, 1=start, 2=end, 5=strand (based on your cut logic)
meta['location_id'] = (
    meta[0].astype(str) + ":" + 
    meta[1].astype(str) + "-" + 
    meta[2].astype(str) + "(" + 
    meta[5].astype(str) + ")"
)

# 4. Merge
merged = pd.merge(meta, seqs, on='location_id', how='inner')

# 5. Drop the temporary merge key and write output
# Your awk script output specific columns + sequence at the end
# We write the original meta columns + sequence
# cols_to_keep = [0, 1, 2, 5, 3, 4, 6, 7, 8, 9, 10, 11, 'sequence']
cols_to_keep = [0, 1, 2, 5, 3, 4, 'sequence']
final_df = merged[cols_to_keep]
final_df.to_csv(snakemake.output.tsv, sep='\t', header=False, index=False)