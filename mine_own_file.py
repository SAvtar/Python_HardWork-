
# # Load the text file
# def text_file():
#     global file
#     file = open('/mnt/745AA3875AA34528/SOFTWARES/How_to_make_a_text_summarizer-master/bbc/business/001.txt')
#     file = file.read()
#     file = list(file.split('\n'))
#     for line in file:
#         print(line)
#     words = []
#
# text_file()
#
#
# # Removing the unwanted words
# import io
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from collections import Counter
# #word_tokenize accepts a string as an input, not a file.
# stop_words = set(stopwords.words('english'))
# file1 = open("/mnt/745AA3875AA34528/SOFTWARES/How_to_make_a_text_summarizer-master/bbc/business/001.txt")
# line = file1.read()# Use this to read file content as a stream:
# words = line.split()
# for r in words:
#     if not r in stop_words:
#         appendFile = open('filteredtext.txt','a')
#         appendFile.write(" "+r)
#         appendFile.close()
# Words = [Words for line in file1 for Words in line.split()]
# print ("The total word count is:", len(words))
# # now use collections.Counter
# c = Counter(words)
# for word, count in c.most_common():
#     print (word, count)

# ==========================================================================================================================================================
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

# Removing the unwanted words
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("/mnt/745AA3875AA34528/SOFTWARES/How_to_make_a_text_summarizer-master/bbc/business/001.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('File_With_Removed_Words.txt','a')
        appendFile.write(" "+r)
        appendFile.close()
