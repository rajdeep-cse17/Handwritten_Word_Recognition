from __future__ import print_function

# Execute using py3_tf1 environment
import os

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import tensorflow as tf
import numpy as np
from PIL import Image  
import PIL  
import random
import cv2
import time
import h5py
import editdistance
import pickle

def preprocess(img2):
    [r,c]=img2.shape
    #print(img2)
    img3=img2
    (thresh,img)=cv2.threshold(img3,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    [r,c]=img.shape
    changeover=[]
    sum=0
    cnt=0
    for i in range(r):
        chng=0
        for j in range(c-1):
            if (img[i,j]==0 and img[i,j+1]==255) or (img[i,j]==255 and img[i,j+1]==0):
                chng=chng+1
        changeover.append(chng)
        sum=sum+chng
        if chng!=0:
            cnt=cnt+1
   # print(changeover)

    if cnt==0:
        return img3
    avg=sum/cnt
    #print(avg)
    for i in range(r):
        if changeover[i]>avg:
            img3=img3[i:,:]
            break;
    return img3
    '''print(img.shape)
    cv2.imwrite('/home/cmater/Rajdeep/handwriting_recognition/a.png',img)
    print('Image write successful')'''


def valley(img2):
    #img3=preprocess(img2)
    (thresh,img)=cv2.threshold(img2,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
   # print(img)
    [r,c]=img.shape
    valleys=[]
    count=0
    sum=0
    max=-1
    min=10000
    for i in range(c):
        firstdp=-1
        for j in range(r):
            if img[j,i]==255:
                firstdp=j
                if firstdp>max:
                    max=firstdp
                if firstdp<min:
                    min=firstdp
                break
        if firstdp!=-1:
            sum=sum+firstdp
            count=count+1
        else:
            sum=sum+r
            count=count+1
    avg=sum/count
#    print(avg)
    if max==min:
        fuzzy=np.zeros(c)
    else:
        fuzzy=[]
        for i in range(c):
            firstdp=-1
            for j in range(r):
                if img[j,i]==255:
                	firstdp=j
                	fuzzy.append((firstdp-min)/(max-min))
               		break
            #print(firstdp)
            #print('\n')
            if firstdp==-1:
                fuzzy.append(1)
    avg_fuzzy=np.sum(fuzzy)
    avg_fuzzy=avg_fuzzy/len(fuzzy)
    for i in range(len(fuzzy)):
    	if fuzzy[i]<avg_fuzzy:
    		fuzzy[i]=0
    return ((fuzzy))

with h5py.File('/home/cmater/Rajdeep/handwriting_recognition/data/IAM/IAM_words_48_192.hdf5', "r") as hdf5_f:
    img    = np.copy(hdf5_f.get('X_'+'trn'))



for i in range(img.shape[0]):
	#cv2.imwrite('/home/cmater/Rajdeep/handwriting_recognition/data/IAM/valley_output/original/'+str(i)+'.png',img[i])
	print(i)
	print('\n')
	img_x=img[i]
        #cv2.imwrite('/home/cmater/Rajdeep/handwriting_recognition/b.png',img[0])
	fuzzy=np.array(valley(img_x))
	img[i]=img[i]*(1.0-fuzzy)
	cv2.imwrite('/home/cmater/Rajdeep/handwriting_recognition/data/IAM/valley_output/modified_without_preprocess_with_avggreater/'+str(i)+'.png',img[i])
