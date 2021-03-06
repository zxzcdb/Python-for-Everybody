# Welcome XINGZHOU ZHU from Using Python to Access Web Data
# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#     Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 87 values with a sum=445822)
#     Actual data: http://python-data.dr-chuck.net/regex_sum_245924.txt (There are 82 values and the sum ends with 286)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:
# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative 
# 7 and rewarding activity.  You can write programs for 
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that 
# everyone needs to know how to program ...
# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers. 

# Import packages
import re
import urllib.request

# Open data file
url = 'http://python-data.dr-chuck.net/regex_sum_245924.txt'
txt = urllib.request.urlopen(url)
cont = txt.read().decode(encoding='utf-8')
# txt = open('C:/Users/te121877/regex_sum_245924.txt',encoding='utf-8')
# cont = txt.read()
# cont

#Execute
num = re.findall('[0-9]+',cont)
result = sum(int(i) for i in num)
print(result)
#368286

# Easier method
# print(sum(int(i) for i in re.findall('[0-9]+',urllib.request.urlopen('http://python-data.dr-chuck.net/regex_sum_245924.txt').read())))
print(sum(int(i) for i in re.findall('[0-9]+',open('C:/Users/te121877/regex_sum_245924.txt',encoding='utf-8').read())))
