#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Converts FASTA to csv',
                                 epilog='The program works with single line FASTA files')

parser.add_argument('-f', metavar='', required=True, help='Input single line FASTA file')
parser.add_argument('-o', metavar='', required=True, help='Output csv file')
parser.add_argument('-option', metavar='', default='aa',
                    help='Enter nuc for Nucleotide sequence [default aa for Protein sequence')
parser.add_argument('-mb', action='store_true',
                    help='Use this flag if sequences are composed of only the codon middle bases')

args = parser.parse_args()

if __name__ == '__main__':
    with open(args.f, 'r') as fopen:
        name = []
        fasta = []

        for line in fopen:
            if line.startswith('>'):
                name.append(line.rstrip()[1:])
            else:
                if args.option == 'nuc':
                    fasta.append(line.rstrip().lower())
                else:
                    fasta.append(line.rstrip())

    skip = 1

    if args.option == 'nuc':
        if not args.mb:
            skip = 3

    split_fasta = []

    for _ in range(len(fasta)):
        split_fasta.append([])
        for i in range(0, len(fasta[_]), skip):
            split_fasta[_].append(fasta[_][i:i + skip])

    fout_seq = open(args.o, 'w')

    for i in range(len(split_fasta)):
        fout_seq.write('%s,' % name[i])
        for j in range(len(split_fasta[i])):
            if j != len(split_fasta[i]) - 1:
                fout_seq.write('%s,' % split_fasta[i][j])
            else:
                fout_seq.write('%s\n' % split_fasta[i][j])

    fout_seq.close()
