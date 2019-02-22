#!/usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser(description='Converts an amino acid FASTA to codon middle base FASTA',
                                 epilog='S is assigned c or g based on its frequency of occurrence in nature')

parser.add_argument('-f', metavar='', help='Input single line amino acid FASTA')
parser.add_argument('-o', metavar='', help='Output single line codon middle base FASTA')

args = parser.parse_args()

middle_base_dict = {'A': 'c', 'C': 'g', 'D': 'a', 'E': 'a', 'F': 't', 'G': 'g', 'H': 'a', 'I': 't', 'K': 'a', 'L': 't',
                    'M': 't', 'N': 'a', 'P': 'c', 'Q': 'a', 'R': 'g', 'T': 'c', 'V': 't', 'W': 'g', 'Y': 'a', '-': '-'}

if __name__ == '__main__':
    with open(args.f, 'r') as fopen:
        aa_fasta = [line.rstrip() for line in fopen]

    fout = open(args.o, 'w')

    for _ in range(len(aa_fasta)):
        if not _ % 2 == 0:
            temp = []
            for i in range(len(aa_fasta[_])):
                aa = aa_fasta[_][i:i+1]
                if aa == 'S':
                    random_number = random.random()
                    if random_number > 0.6:
                        mb = 'g'
                    else:
                        mb = 'c'
                else:
                    mb = middle_base_dict[aa]
                temp.append(mb)
            fout.write('%s\n' % "".join(temp))
        else:
            fout.write('%s\n' % aa_fasta[_])

    fout.close()
