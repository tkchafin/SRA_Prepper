# SRA_Prepper
scripts for prepping files for SRA upload

Not complete -- will eventually finish -- probably next time I have to upload to SRA ... :(

FTP notes:

NOTE: Can't do this on AHPCC (FTP not enabled). Douglas Lab users can use the camel1 server. 

```
#connect using ftp (note the -p)
ftp -p ftp-private.ncbi.nlm.nih.gov

#will be prompted for username/ password -- you will receive these in the SRA submission wizard portal
#follow instructions to get to your upload directory 

#in the upload directory, e.g. uploads/<user-specific>/fastq
#turn off option to be prompted for each file
prompt

#upload all files e.g. ending with .fq.gz
mput *.fq.gz

#might take a while, recommend doing all of this in a tmux session

```
