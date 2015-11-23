#!/usr/bin/env python
import os, shutil, glob
from os import path
from optparse import OptionParser
from pprint import pprint

def main():
   usage = 'usage: %prog [options] dir1 dir2 dir3'
   usage = 'usage: %prog [options] dir*'
   usage = 'usage: %prog [options] dir/subdir*'
   parser = OptionParser(usage)
   parser.add_option('-f', '--filenames' , dest='filenames',
                     help='comma-sep list of filenames to gather',
                     default=None, type='string')
   parser.add_option('-o', '--outDir' , dest='outDir',
                     help='destination for output files',
                     default='', type='string')
   (opt, args) = parser.parse_args()

   if not opt.outDir:
      opt.outDir = path.join(path.dirname(args[0]), 'gathered')

   togather = opt.filenames.split(',')
   print "will gather:", togather
   print "will save to:", opt.outDir
   try: os.makedirs(opt.outDir)
   except OSError: pass

   gathered = []
   for dname in args:
      if not path.isdir(dname): continue
      for fn in togather: gathered += glob.glob(path.join(dname,fn))

   print "gathered files:"
   pprint(gathered)

   raw_input("Press key to continue...")

   for fname in gathered:
      base,ext = path.splitext(path.basename(fname))
      tag  = path.split(path.dirname(fname))[-1]
      targetname = "%s_%s%s" % (base,tag,ext)
      shutil.copy2(fname, path.join(opt.outDir, targetname))

   return 0



if __name__ == '__main__':
    exit(main())