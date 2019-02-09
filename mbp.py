#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Computes fwd-fwd and fwd-rev MBP scores for a list of FASTA files')

parser.add_argument('-f', metavar='', required=True, help='List of FASTA files')
parser.add_argument('-mb', action='store_true',
                    help='Use this flag if the sequences are composed of only codon middle bases')
parser.add_argument('-sequence', action='store_true',
                    help='Use this flag if individual sequence level MBP scores should be outputted')

args = parser.parse_args()


def read_fasta(filename):
    with open(filename, 'r') as fopen:
        seq_name = []
        sequence = []

        for line in fopen:
            if line.startswith('>'):
                seq_name.append(line.rstrip()[1:])
            else:
                sequence.append(line.rstrip().lower())

    return seq_name, sequence


def mbpf(seq_1, seq_2, comp):
    count = 0
    dashes = 0

    for _, nuc in enumerate(seq_1):
        if nuc == '-' or seq_2[_] == '-':
            dashes += 1
        elif comp[nuc] == seq_2[_]:
            count += 1

    return count / (len(seq_1) - dashes)


if __name__ == '__main__':
    with open(args.f, 'r') as fopen:
        file_list = [line.rstrip() for line in fopen]

    base_comp = {'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}

    fout_all = open('mbp_out', 'w')
    fout_all.write('Fasta 1,Fasta 2,<MBP> fwd-fwd,<MBP> fwd-rev\n')

    for i in range(len(file_list)):
        fasta_i_name = file_list[i]
        fasta_org_name_i, fasta_i = read_fasta(fasta_i_name)

        if not args.mb:
            mb_fasta_i = [fasta_i[_][1::3] for _ in range(len(fasta_i))]
        else:
            mb_fasta_i = fasta_i

        for j in range(i, len(file_list)):
            same_fasta = False
            if i == j:
                fasta_j_name = fasta_i_name
                fasta_j = fasta_i
                fasta_org_name_j = fasta_org_name_i
                mb_fasta_j = mb_fasta_i
                same_fasta = True
            else:
                fasta_j_name = file_list[j]
                fasta_org_name_j, fasta_j = read_fasta(fasta_j_name)

                if not args.mb:
                    mb_fasta_j = [fasta_j[_][1::3] for _ in range(len(fasta_j))]
                else:
                    mb_fasta_j = fasta_j

            name = []
            fwd = []
            rev = []

            for x in range(len(mb_fasta_i)):
                if same_fasta:
                    for y in range(x, len(mb_fasta_j)):
                        name.append([str(fasta_org_name_i[x]), str(fasta_org_name_j[y])])
                        fwd.append(mbpf(mb_fasta_i[x], mb_fasta_j[y], base_comp))
                        rev.append(mbpf(mb_fasta_i[x], mb_fasta_j[y][::-1], base_comp))
                else:
                    for y in range(len(mb_fasta_j)):
                        name.append([str(fasta_org_name_i[x]), str(fasta_org_name_j[y])])
                        fwd.append(mbpf(mb_fasta_i[x], mb_fasta_j[y], base_comp))
                        rev.append(mbpf(mb_fasta_i[x], mb_fasta_j[y][::-1], base_comp))

            if args.verbose:
                fout_name = fasta_i_name.split('.')[0] + '-' + fasta_j_name.split('.')[0]
                fout = open(fout_name, 'w')

                fout.write('Seq 1,Seq 2,MBP fwd-fwd,MBP fwd-rev\n')
                for _ in range(len(name)):
                    fout.write('%s,%s,%f,%f\n' % (name[_][0], name[_][1], fwd[_], rev[_]))

                fout.close()

            mean_fwd = sum(fwd) / len(fwd)
            mean_rev = sum(rev) / len(rev)

            fout_all.write(
                '%s,%s,%f,%f\n' % (fasta_i_name.split('.')[0], fasta_j_name.split('.')[0], mean_fwd, mean_rev))

    fout_all.close()
