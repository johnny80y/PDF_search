#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
####  PDF Search Tool  ####

Created on Sun Nov 15 11:31:03 2020

@author: johnny80y
"""


"""
Goal:
I want to be able to find passages in a pdf file searching by word clusters. Basically, I want to search a PDF and find sections/pages where certain words are clustered together.

For example, I want to input a PDF file and a word list and if there's a place where 5 out of X words in my word list appear in close proximity, I want to find that. This means, I don't just want to search for individual terms but for clusters of random subsets of wordlists.

I want to make this a command-line tool. My script will take two arguments: a pdf-file and a word-list. Maybe it will also take a number that will tell the script how many of the words it needs to match on any given paragraph to indicate a hit (this would basically allow the user to widen/narrow the search scope).

I need my script to be able to extract text from a PDF.

I need my script to read in a word-list from a .txt file.

I need to make the tool usable through command-line inputs.

The output I want is the page number and maybe a print-out of the section of the text where the matches were found.
"""

import pyPDF2 as p2
#reader = PyPDF2.PdfFileReader('honeyBadgerWiki.pdf')



