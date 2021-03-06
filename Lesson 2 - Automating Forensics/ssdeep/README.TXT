SSDEEP(1)                     SSDEEP COMMAND                     SSDEEP(1)

NAME
       ssdeep - Computes context triggered piecewise hashes (fuzzy hashes)

SYNOPSIS
       ssdeep [-m <file>] [-k <file>] [-vdprgsblcxa] [-t val] [FILES]
       ssdeep [-V|h]

DESCRIPTION
       Computes  a  signature  based on context triggered piecewise hashes
       for each input file, also called a fuzzy hash.  If  requested,  the
       program matches those signatures against a file of known signatures
       and reports any possible matches.  It can also examine one or  more
       files of signatures and find any matches in those files.  Output is
       written to standard out and errors to standard error.

       -m <file>
              Loads the specified file of known  hashes  to  be  used  for
              matching.  This  file  must be a previous output of the pro‐
              gram. The program then hashes each entry in FILES  and  com‐
              pares these signatures to the known signatures.  Any matches
              which score above the threshold are  displayed.   This  flag
              may  be  used  multiple times to load more known signatures.
              This flag may not be used with the -k or -x flags.

       -k <file>
              Load the specified file of  known  hashes  to  be  used  for
              matching.  This  file  must be a previous output of the pro‐
              gram. The program then treats each entry in FILES as  a  set
              of  known hashes as well. The hashes in these FILES are com‐
              pared to the known hashes  from  this  file.  Matches  which
              score above the threshold are displayed. Both the file spec‐
              ified here and the input FILES should contain fuzzy  hashes.
              This flag may be used multiple times to load more known sig‐
              natures.  This flag may not be used with the -m, -d,  or  -p
              flags.

       -v     Verbose  mode.  The name of each file is printed to standard
              error as it is being hashed.

       -d     Computes a signature for each entry in the  FILES  and  com‐
              pares it to the set of known signatures. Matches which score
              above the threshold are displayed. The computed signature is
              then  added  to  the set of known signatures.  This flag may
              not be used with the -k or -x flags.

       -p     Works like the -d flag, but displays all  matches  for  each
              file. That is, for two files A and B which match score above
              the threshold, displays "A matches B"  and  "B  matches  A".
              This flag may not be used with the -k or -x flags.

       -r     Enables  recursive  mode.  All subdirectories are traversed.
              Please note that recursive mode cannot be  used  to  examine
              all  files  of a given file extension. For example, invoking
              the program with -r *.txt will examine all files in directo‐
              ries  that end in .txt.  If you want to process all files in
              a directory tree with the .txt suffix, try using the find(1)
              command.

       -g     Similar  files  are grouped together into clusters. This can
              be handy for finding more similar files. That is, if you are
              searching  for  file  A,  which  matches  B,  anything which
              matches B will also be included in the cluster.

       -s     Silent mode. All error messages are suppressed.

       -b     Enables bare mode. Strips any leading directory  information
              from displayed filenames.  This flag may not be used in con‐
              junction with the -l flag.

       -l     Enables relative file paths. Instead of printing  the  abso‐
              lute  path for each file, displays the relative file path as
              indicated on the command line. This flag may not be used  in
              conjunction with the -b flag.

       -c     Enables  comma separated output mode. In any of the matching
              modes -d, -p, or -m, displays the  results  as  input  file,
              known file, matching score.

       -x     Signature  file  matching.  Each entry in FILES must contain
              signatures generated by a previous output  of  the  program.
              Each  signature  is  loaded  and compared against the set of
              known hashes. Match scores  above  the  threshold  are  dis‐
              played.  Each  signature is then added to the set of knowns.
              This flag may not be used with the -m, -d, or -p flags.

       -a     Displays all matches in any of the matching mode, regardless
              of  score.   Using the -a flag displays all results, even if
              the match score is zero.

       -t <val>
              In any of the matching  modes,  only  display  matches  when
              match  score  is  greater  than the given value. The default
              threshold value is zero.

       -h     Show a help screen and exit.

       -V     Show the version number and exit.

RETURN VALUE
       Returns 0 on success, 1 if there is a problem.  Read  errors,  per‐
       mission denied, and encountering directories while not in recursive
       mode are still considered successes. Problems are things like being
       unable to load the matching file, specifying both bare and relative
       paths, etc.

AUTHOR
       ssdeep was written by Jesse Kornblum of Facebook,
       research@jessekornblum.com

COPYRIGHT
       Copyright (C) 2002 Andrew Tridgell
       Copyright (C) 2006, 2008, 2010 ManTech International Corporation
       Copyright (C) 2012 Kyrus
       Copyright (C) 2013 Helmut Grohne
       Copyright (C) 2013, 2014 Facebook
       Copyright (C) 2014 kikairoya
       Copyright (C) 2014 Jesse Kornblum
       Copyright (C) 2017 Tsukasa OI

       This program is licensed under the  terms  of  the  General  Public
       License.  See the file COPYING for details.

SEE ALSO
       This program is based on SpamSum by Dr. Andrews Tridgell.
       http://www.samba.org/ftp/unpacked/junkcode/spamsum/

ssdeep Project          Version 2.14.1 - 7 Nov 2017              SSDEEP(1)
