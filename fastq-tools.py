#!/usr/bin/env python
#coding=utf8
import os,sys,re
import argparse

def parse_args():
	parse = argparse.ArgumentParser(description='This script is used to transform the fastq/fasta file')
	parse.add_argument('-i','--input',action='store',required=True,help='input fastq/fasta file')
	parse.add_argument('-t','--type',action='store',default='fastq',help='input file type:fastq(default) or fasta')
	parse.add_argument('-mm','--method',action='store',required=True,choices=['reverse','reverse_complement','fastq2fasta','fasta2fastq'],help='the transform method')
	parse.add_argument('-v','--verbose',action='store_true',default=False,help='if ouput log messages(default:False)')
	parse.add_argument('-o','--output',action='store',required=True,help='output file name')
	args = parse.parse_args()
	return args
args = parse_args()
print('Parse arg module test begins')
print('--input:\t%s' %args.input)
print('--type:\t%s' %args.type)
print('--method:\t%s' %args.method)
print('--verbose:\t%s' %args.verbose)
print('--output:\t%s' %args.output)
print('Parse arg module test ends')
