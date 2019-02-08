#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Maps the nucleotide sequence to aligned amino acid sequence')

parser.add_argument('-n', metavar='', help='Input Nucleotide FASTA file')
parser.add_argument('-a', metavar='', help='Input Aligned amino acid FASTA file')
parser.add_argument('-o', metavar='', help='Output Aligned nucleotide FASTA file')

args = parser.parse_args()


def build_dict(fasta, skip):
    fasta_dict = {}
    name = ""
    for _ in range(len(fasta)):
        temp = []
        if fasta[_].startswith('>'):
            name = fasta[_]
        else:
            for i in range(0, len(fasta[_]), skip):
                temp.append(fasta[_][i:i+skip])
            fasta_dict[name] = temp

    return fasta_dict


if __name__ == '__main__':
    with open(args.n, 'r') as fopen:
        nuc_fasta = [line.rstrip() for line in fopen]

    with open(args.a, 'r') as fopen:
        aa_align_fasta = [line.rstrip() for line in fopen]

    nuc_dict = build_dict(nuc_fasta, 3)
    aa_align_dict = build_dict(aa_align_fasta, 1)
