#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Converts multi line FASTA file to single line FASTA file')

parser.add_argument('-f', metavar='', help='Input multi line FASTA file')
parser.add_argument('-o', metavar='', help='Output single line FASTA line')

args = parser.parse_args()


if __name__ == '__main__':
    with open(args.f, 'r') as fopen:
        multi_line_fasta = [line.rstrip() for line in fopen]

    single_line_fasta = []

    for _ in range(len(multi_line_fasta)):
        if multi_line_fasta[_].startswith('>'):
            single_line_fasta.append(multi_line_fasta[_])
            single_line_fasta.append([])
        else:
            single_line_fasta[-1].append(multi_line_fasta[_])

    fout = open(args.o, 'w')

    for _ in range(len(single_line_fasta)):
        if not _ % 2 == 0:
            single_line_fasta[_] = "".join(single_line_fasta[_])

        fout.write('%s\n' % single_line_fasta[_])



