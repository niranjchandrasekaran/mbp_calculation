#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Converts csv to single line FASTA')

parser.add_argument('-f', metavar='', help='Input csv file')
parser.add_argument('-n', metavar='', help='Input FASTA names')
parser.add_argument('-o', metavar='', help= 'output FASTA file')

args = parser.parse_args()


if __name__ == '__main__':
    with open(args.n, 'r') as fopen:
        names = [line.rstrip() for line in fopen]

    with open(args.f, 'r') as fopen:
        csv = [line.rstrip().split(',') for line in fopen]

    fout = open(args.o, 'w')

    for _ in range(len(names)):
        fout.write('>%s\n' % names[_])
        fout.write('%s\n' % ("".join(csv[_])))

    fout.close()
