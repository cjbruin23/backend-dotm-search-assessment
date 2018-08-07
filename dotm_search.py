#!/usr/bin/env python
"""
Given a directory path, this searches all files in the path for a given text string 
within the 'word/document.xml' section of a MSWord .dotm file.
"""

import os
import sys
import glob
import zipfile

cwd = os.getcwd() + '/dotm_files/'

# Your awesome code begins here!
def decodeDOTM(text, pathway=cwd):
    total_files_searched = 0
    files_matched = 0

    print pathway

    for filename in glob.iglob(pathway + '/*.dotm'):
        zf = zipfile.ZipFile(filename, 'r')
        data = zf.read('word/document.xml')
        total_files_searched += 1
        if text in data:
            output_string = ''
            files_matched += 1
            root_index = data.index(text)
            output_string += 'Match found in file ' + filename + '\n' 
            output_string += '\t...' + data[root_index - 40:root_index + 40] + '...'
            print output_string
        
    print "Total files searced: " + str(total_files_searched)
    print "Files matched: " + str(files_matched)
    print

    return


if __name__ == "__main__":
    text = sys.argv[1]
    print sys.argv
    if len(sys.argv) == 2:
        decodeDOTM(text)
    elif len(sys.argv) == 4 and sys.argv[2] == '--dir':
        new_path = sys.argv[3]
        decodeDOTM(text, new_path)  
    else:
        print 'unknown command'
        sys.exit(1)
        
