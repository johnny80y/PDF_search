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

# I wanted to use pdPDF2 but after two days of trying,I couldn't get it 
# running on my laptop. No idea why though.


# As my python script keepy changing the default directory in which it looks 
# for my pdfs, I manually set the working directory to the directory in which
# this script file is saved:
import os
cwd = os.getcwd()
os.chdir(cwd)


# <<<<<----------     Convert PDF to Text     ---------->>>>>

from tika import parser   

# As I cannot extract text page by page from a pdf using tika, I first 
# convert the file to an xml file and the split it using html-tags
# https://www.geeksforgeeks.org/parsing-pdfs-in-python-with-tika/
# https://stackoverflow.com/questions/53093531/python-apache-tika-single-page-parser

raw_xml = parser.from_file("pages.sample.pdf", xmlContent=True) # convert pdf to xml
body = raw_xml['content'].split('<body>')[1].split('</body>')[0] # split into pages using tags
body_without_tag = body.replace("<p>", "").replace("</p>", "").replace("<div>", "").replace("</div>","").replace("<p />","")
text_pages = body_without_tag.split("<div class=\"page\">")[1:]


num_pages = len(text_pages) # how many pages do I have?
print(num_pages)
print('dirty text: ', text_pages)


type(text_pages) # >>> list
# my goal now is to remove the \n characters from my strings:
clean_text = [sub.replace('\n', '') for sub in text_pages]    
print('cleaned text: ', clean_text)


print("\n") # line break in output


# <<<<<----------     Search for Substring in String-List     ---------->>>>>

# I now have a list of strings and each string represents one page.
# I now want to search for a single term and obtain the page on which it can
# be found
# https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/

# The substring I will be searching for = my search term:
key = 'J'

# result = [i for i in clean_text if key in i] # finds the list-item containing the key
# At first, I used this list comprehension but it only finds the first instance
# of a matching substring and then stops. If multiple list
# items contain the string, it only finds one

# This lambda function finds all list items that contain my substring-key:
result1 = list(filter(lambda x: key in x, clean_text)) 
print(result1) # --> Jessy, Jakob, Johannes



# Search for the next key only within the subset of list items that already
# had the first key:
key2 = "o"  # --> filter out Jessy
result2 = list(filter(lambda x: key2 in x, result1))
print(result2)  # --> Jakob & Johannes


# Get page-number in original list for my result:
    # remember that pages start counting at 1 and list 
    # indices start counting at 0. Thus, the page number
    # for a list item is its index+1
#print("My result page number is: ", clean_text.index(result2[0]) + 1)
    # This only works for a single result. If I had multiple pages as results,
    # this would fail.
    # Also, if I had no results, this would fail.


# <<<<<----------     Get Page Numbers for Search-Results     ---------->>>>>

# I want to get the page numbers for ALL pages that match my search query:

# Define a function that takes two arguments: a list and a list item.
# The function then returns the index number of that list item.
def ind(L, i):
    v = L.index(i)
    #print(v)
    return v


# This for-Loop matches up the items in the sublist with the larger list.
# clean_text is the whole list and result2 is a subset of that list.
# Each item contained in the sublist is also contained in the larger list.
# This for-loop gives me the index-numbers for the larger list. These
# index numbers then correspond to the page numbers in the PDF.
# Since list indices start at 0 and PRF-ages start at 1, I need to add 1 to
# the index:
for i in result2:
    x = ind(result2, i)         # get index number for item i in sublist
    y = clean_text.index(result2[x])  # get the corresponding index number for the larger list
    y += 1                      # add one to the index number
    print(y)                    # print the result    

# >>> eturns 3 and 6 --> perfect!!





















# TODO:
    # I want to implement the ability to search for several terms at once and
    # to only return those pages that return all of them. 
    # Later I also want to implement clusters, where not all but some of the
    # search terms need to be present.
    
    # Fr now, however, I will search for those pages, that contain all search
    # terms at least once.
    # I can implement this by searching for term 1 and then saving a sublist
    # of only those items that contained term1.
    # Then  search that sublist for term2 and remove all those items that
    # don't ontain term2.
    # This way, I would continuallyeliinate list items until only those remain
    # that ontain all search terms.