#!/usr/bin/python3
import argparse
import os
from Tux.Clean import Clean
from Tux.Create import Create
from Tux.Init import Init
from Tux.Sort import SilentSort


def main():

   parser = argparse.ArgumentParser()
   subparsers = parser.add_subparsers(dest='command', help="sub-command that are called along with tux, they will take you to the the program you wish to have executed.")


   # creating the arguments to be passed for the 'tux create' command
   create_parser = subparsers.add_parser('create', aliases=['cr'], help="used to create a new script, make it executable, and place it in the correct directory")
   create_parser.add_argument("baseName", help="the basename of your new file")
   fileType_parser = create_parser.add_mutually_exclusive_group()
   fileType_parser.add_argument('-p', '--python', action='store_const', dest='fileType', const='python', help="Create a python file")
   fileType_parser.add_argument('-s', '--bash', action='store_const', dest='fileType', const='bash', help="Create a bash file")
   fileType_parser.add_argument('-r', '--rust', action='store_const', dest='fileType', const='rust', help="Create a rust file")
   fileType_parser.add_argument('-c', '--css', action='store_const', dest='fileType', const='css', help="Create a css file")
   fileType_parser.add_argument('-w', '--html', action='store_const', dest='fileType', const='html', help="Create a html file")
   fileType_parser.add_argument('-j', '--jss', action='store_const', dest='fileType', const='jss', help="Create a JavaScript file")
   fileType_parser.add_argument('-y', '--yaml', action='store_const', dest='fileType', const='yaml', help="Create a yaml file")
   fileType_parser.add_argument('-d', '--dart', action='store_const', dest='fileType', const='dart', help="Create a dart file")
   fileType_parser.add_argument('-m', '--md', action='store_const', dest='fileType', const='md', help="Create a markdown file")
   fileType_parser.set_defaults(fileType='python')
   destPath_parser = create_parser.add_mutually_exclusive_group()
   destPath_parser.add_argument('-C', '--cwd', dest='destPath', action='store_const', const=os.getcwd(), help='Create the file in the current directory')
   destPath_parser.add_argument('-S', '--Scripts', dest='destPath', action='store_const', const='Scripts', help='Create the file in the Scripts directory')
   destPath_parser.add_argument('-P', '--PracticeScripts', dest='destPath', action='store_const', const='PracticeScripts', help='Create the file in the PracticeScripts directory')
   destPath_parser.set_defaults(destPath=os.getcwd())

   # create the arguments for the 'tux init' command
   init_parser = subparsers.add_parser('init', aliases=['in'], help="Initialize a script, file will be send to ~/.local/bin where it can be called from the command line")
   init_parser.add_argument('fileName', help="the File to be turned into a script")


   # create the arguments for the 'tux clean-dir' command
   clean_parser = subparsers.add_parser('clean', aliases=['cd'], help='Clean and sort the files in the specified directory with some commandline interaction')
   clean_parser.add_argument('srcPath', nargs='?', default='.', type=str, help="the directory to be cleaned and sorted")
   clean_parser.add_argument('-i', '--ignoredFiles', nargs='*',help="files to be ignored in the directory in the form '*.py' or '*hogan*' lowercase")


   # create the  'tux silent-sort' method 
   sort_parser = subparsers.add_parser('sort', aliases=['ss'], help="like the clean command but silently done with no interaction")
   sort_parser.add_argument('srcPath', nargs='?', default='.', type=str, help="the directory to be cleaned and sorted")
   sort_parser.add_argument('-i', '--ignoredFiles', nargs='*', help="files to be ignored in the directory in the form '*.py' or '*hogan*' lowercase")

   try:
      args = parser.parse_args()
   except SystemExit:
      parser.print_help()
      raise

   # deciding the directory to create file in
   if args.command == 'clean':
      Clean(**vars(args))
   if args.command == 'create':
      Create(**vars(args))
   if args.command == 'init':
      Init(**vars(args))
   if args.command == 'sort':
      SilentSort(**vars(args))
   # else:
   #    parser.print_help()
       

if __name__ == "__main__":
   main()

