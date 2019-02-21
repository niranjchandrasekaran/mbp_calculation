#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Maps the nucleotide sequence to aligned amino acid sequence')

parser.add_argument('-n', metavar='', required=True, help='Input single line Nucleotide FASTA file')
parser.add_argument('-a', metavar='', required=True, help='Input single line Aligned amino acid FASTA file')
parser.add_argument('-o', metavar='', required=True, help='Output single line Aligned nucleotide FASTA file')
parser.add_argument('-mb', action = 'store_true',
                    help='Use this flag if the nucleotide sequences are composed of only codon middle bases')

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
                temp.append(fasta[_][i:i + skip])
            fasta_dict[name] = temp

    return fasta_dict


if __name__ == '__main__':
    with open(args.n, 'r') as fopen:
        nuc_fasta = [line.rstrip() for line in fopen]

    with open(args.a, 'r') as fopen:
        aa_align_fasta = [line.rstrip() for line in fopen]

    if not args.mb:
        nuc_dict = build_dict(nuc_fasta, 3)
    else:
        nuc_dict = build_dict(nuc_fasta, 1)

    aa_align_dict = build_dict(aa_align_fasta, 1)

    nuc_align_fasta = []

    for seq in aa_align_dict:
        nuc_align_fasta.append(seq)
        count_dashes = 0
        temp = []
        for i in range(len(aa_align_dict[seq])):
            if aa_align_dict[seq][i] != '-':
                temp.append(nuc_dict[seq][i - count_dashes])
            else:
                count_dashes += 1
                if not args.mb:
                    temp.append('---')
                else:
                    temp.append('-')

        nuc_align_fasta.append("".join(temp))

    fout = open(args.o, 'w')

    for _ in range(len(nuc_align_fasta)):
        fout.write('%s\n' % nuc_align_fasta[_])

    fout.close()
