# MBP calculation
This project consists of scripts that were used to generate codon middle base pairing (MBP) frequencies in 
[this study](https://academic.oup.com/mbe/article/30/7/1588/973415) where we provided evidence supporting the 
hypothesis  that class I and class II aminoacyl t-RNA synthetases evolved from the opposite strands of the same 
ancestral gene.

To compute MBP with these scripts, it is necessary to have the amino acid sequence of the enzyme in the 
[FASTA](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=BlastHelp) format and the 
corresponding nucleotide sequence, also in the same format. Each FASTA file may contain sequences from multiple 
organisms.

The first step of the analysis is to align the protein sequences from the different organisms. We used 
[MUSCLE](https://www.ebi.ac.uk/Tools/msa/muscle/) in our study. But other Multiple Sequence Alignment (MSA) tools can 
also be used to generate the aligned amino acid FASTA file.

The aligned FASTA files usually contain sequences written over several lines. The script **single_line_fasta.py** 
converts such files to single line FASTA files. This is essential for the remaining scripts to work. All scripts in 
this project can be run with only the '**-h**' flag to display the help menu. For example running 
**single_line_fasta.py** with the '**-h**' flag 

```
single_line_fasta.py -h
```

shows the following.

```
usage: single_line_fasta.py [-h] -f  -o

Converts multi line FASTA file to single line FASTA file

optional arguments:
  -h, --help  show this help message and exit
  -f          Input multi line FASTA file
  -o          Output single line FASTA line
```

The script takes a multi line FASTA file as input and outputs a single line file. 

Next, the nucleotide sequence has to be mapped back to the aligned protein sequence. This is done using the 
**map_nuc_to_aa.py** script. It takes the nucleotide FASTA file and the aligned amino acid FASTA file as input and 
outputs the aligned nucleotide FASTA file. There is a provision to use only the codon middle bases in the nucleotide 
FASTA file using the '**-mb**' flag. 

Often, it may be necessary to use a spreadsheet software to edit the aligned FASTA files (for example, only a fragment 
of the protein is of interest) or simply visualize the alignment. If the alignment files are edited using the 
spreadsheet software, it is necessary to edit both the amino acid aligned FASTA and nucleotide aligned FASTA 
simultaneously. To help this process, the **fasta_to_csv.py** script converts FASTA files to the CSV format, which can 
be readily read by any spreadsheet software. This script accepts a FASTA file as input and outputs a CSV file. The 
'**-option**' flag specifies whether the input FASTA file is a nucleotide FASTA file (**-option nuc**) or 
an amino acid FASTA file (**-option aa**). The '**-mb**' is included if the nucleotide FASTA file consists of only the 
codon middle bases. The code also outputs the names of the organisms in a separate file which will be useful to 
reconstruct a FASTA file fom the CSV format after it has been modified using the spreadsheet software.

The script **csv_to_fasta.py** converts the CSV file to a FASTA file. It accepts a CSV file along with the names of the 
organism outputted by the previous script.

Finally, the MBP scores are computed using the **mbp.py** script. It takes a text file with a list of FASTA files 
(aligned nucleotide FASTAs) as input and computes the MBP scores as described in the 
[publication](https://academic.oup.com/mbe/article/30/7/1588/973415). The '**-mb**' is included if the nucleotide FASTA 
file consists of only the codon middle bases. The script outputs the all vs. all <MBP> score both in the forward 
direction and in the reverse direction to the file **mbp_out**.  The **-sequence** flag output individual sequence 
level MBP score. Each pair of FASTA file generates a separate output file whose name is derived from the names of the 
pair of FASTA files.