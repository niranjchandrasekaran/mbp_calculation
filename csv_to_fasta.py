#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Converts csv to single line FASTA')

parser.add_argument('-f', metavar='', required=True, help='Input csv file')
parser.add_argument('-o', metavar='', required=True, help='output single line FASTA file')

args = parser.parse_args()


if __name__ == '__main__':
    with open(args.f, 'r') as fopen:
        csv = [line.rstrip().split(',') for line in fopen]

    fout = open(args.o, 'w')

    for _ in range(len(csv)):
        fout.write('>%s\n' % csv[_][0])
        fout.write('%s\n' % ("".join(csv[_][1:])))

    fout.close()
