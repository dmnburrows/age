#Calculate percent of mismatches per read
import pysam as sam
import numpy as np

path = '/cndd3/dburrows/DATA/te/rna/PE.bam/Sample_1105-GABA/Aligned.sortedByCoord.out.bam'

data = sam.AlignmentFile(snakemake.input.inp, 'rb')

mm_v = []
cig_list = []
for x,read in enumerate(data):
    mm_v.append((1-sum(np.asarray(read.cigartuples)[:,1][np.asarray(read.cigartuples)[:,0] == 0]) / read.infer_read_length()) * 100)

#save mm_v as npy file
np.save(snakemake.output.outnpy, mm_v)

