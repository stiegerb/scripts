#! /usr/bin/env python
import subprocess

if __name__ == "__main__":
	usage = """
	Converts all .pdf files in the directory (first argument) to .png
	"""
	from argparse import ArgumentParser
	parser = ArgumentParser(usage)
	parser.add_argument("directory", metavar='file_or_dir', type=str, nargs='+')
	args = parser.parse_args()

	# print args.directory
	from os import path, listdir
	for argument in args.directory:
		for item in listdir(argument):
			if path.isdir(item): continue
			if not path.splitext(item)[1] == '.pdf': continue
			basename = path.splitext(item)[0]
			# print 'calling:',['convert', '-trim', item, basename+'.png']
			subprocess.call(['convert', '-trim', item, basename+'.png'])


