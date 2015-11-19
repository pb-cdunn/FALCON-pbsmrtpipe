"""Work with reads from .fasta files.
"""
#from pbcore.io import FastaReader # see below
from . import functional as func
import collections

def count_read_lengths(fasta):
    """fasta is an input file stream.
    """
    from pbcore.io import FastaReader
    return collections.Counter(len(rec.sequence) for rec in FastaReader(fasta))

def count_read_lengths_fofn(fofn):
    """fofn is an input file stream.
    Return pairs of (length, count).
    """
    hist = collections.defaultdict(int)
    for fn in func.fns_from_fofn(fofn):
        with open(fn) as ifs:
            hist.update(count_read_lengths(ifs))
    return hist.items()

def calc_length_cutoff(size, coverage, i_fofn_fn):
    with open(i_fofn_fn) as fofn:
        pairs = count_read_lengths_fofn(fofn)
        #total = func.total_length(pairs)
        #n50 = func.calc_cutoff(total*.5, pairs)
        target = size*coverage
        cutoff = func.calc_cutoff(target, pairs)
