# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

csvfiles = ['period1.csv','period2.csv','period3.csv','period4.csv','period5.csv','period6.csv']

import nltk
import csv


tweets_period = []
for files in csvfiles:
    list = []
    with open(files, 'rt', encoding = 'utf8') as f:
        reader = csv.reader(f,skipinitialspace = True, delimiter=",",quotechar = "'")
        for row in reader:
            list.append(row)
        
        tweets_period.append(list)
