#!/usr/bin/env python3

from __future__ import print_function
from glob import glob
from os import path

BASE_PATH = path.dirname(path.realpath(__file__))
INPUT_FILEEXTENSION = '.txt'
OUTPUT_FILEEXTENSION = '.sqf'

def parse_file(fp):
	output = []
	for line in fp:
		line = line.rstrip()

		if len(line) == 0:
			continue
		elif line.startswith('this setFace'):
			continue
		elif line.startswith('this setSpeaker'):
			continue
		elif line.startswith('this linkItem "ItemRadioAcreFlagged"'):
			continue
		elif line.startswith('comment'):
			continue
		else:
			output.append(line)

	return output


def write_output_to_file(output, fp):
	for line in output:
		print(line, file=fp)


def main():
	print('Searching in', BASE_PATH)
	matched_files = glob(path.join(BASE_PATH, '*' + INPUT_FILEEXTENSION))

	for file in matched_files:
		print('Converting', file)

		with open(file, 'r') as fp:
			output_content = parse_file(fp)

		with open(file + OUTPUT_FILEEXTENSION, 'w') as fp:
			write_output_to_file(output_content, fp)

if __name__ == '__main__':
	main()

