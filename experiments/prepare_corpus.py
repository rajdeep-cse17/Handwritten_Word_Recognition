#! /usr/bin/env python

# Version withow buckets
# Version 04: Add a restart mechanism
# Execute using py3_tf1 environment


from __future__ import print_function

import tensorflow as tf
import numpy as np
import random
import cv2
import os
import time
import h5py
import editdistance
import pickle
import re

huge_list ={}

with open('IAM_Words.txt', "r") as f:
    for line in f:
    	if(line[0]!='#'):
    		word=re.split(' |\n',line)[-2]
    		if word not in huge_list:
    			huge_list[word]=0
    		huge_list[word]+=1
tot=0
#{k: v for k, v in sorted(huge_list.items(), key=lambda item: item[1])}
new_list=sorted(huge_list.items(), key = lambda x : x[1],reverse=True)
print(len(new_list))
#out = new_list[0: 10000]
b=[a[0] for a in new_list]
#print(b)
pickle.dump( b, open( "save.p", "wb" ) )
