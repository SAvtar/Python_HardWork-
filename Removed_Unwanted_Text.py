
# coding: utf-8

# In[7]:


import os, sys

def main():
   # filepath = sys.argv[1]
   filepath = '/mnt/745AA3875AA34528/SOFTWARES/How_to_make_a_text_summarizer-master/bbc/business/001.txt'

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   bag_of_words = {}
   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   print("Most frequent 10 words {}".format(sorted_words[:10]))

def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1

if __name__ == '__main__':
   main()



# In[8]:


# Removing the Unwanted Words :-

import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("/mnt/745AA3875AA34528/SOFTWARES/How_to_make_a_text_summarizer-master/bbc/business/001.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('File_With_Removed_Unwanted_text.txt','a')
        appendFile.write(" "+r)
        appendFile.close()
Words = [Words for line in file1 for Words in line.split()]

