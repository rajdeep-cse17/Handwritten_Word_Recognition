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
	gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	(thresh,img)=cv2.threshold(gray,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
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
	print(changeover)
	avg=sum/cnt
	print(avg)
	for i in range(r):
		if changeover[i]>avg:
			img2=img2[i:,:]
			break;
	return img2
	'''print(img.shape)
	cv2.imwrite('/home/cmater/Rajdeep/handwriting_recognition/a.png',img)
	print('Image write successful')'''


def valley(img2):
	img2=preprocess(img2)
	gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	(thresh,img)=cv2.threshold(gray,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	[r,c]=img.shape
	valleys=[]
	count=0
	sum=0
	max=-1
	for i in range(c):
		firstdp=-1
		for j in range(r):
			if img[j,i]==0:
				firstdp=j
				if firstdp>max:
					max=firstdp
				break;
		if firstdp!=-1:
			sum=sum+firstdp
			count=count+1
		else:
			sum=sum+r
			count=count+1
	avg=sum/count
	print(avg)
	for i in range(c):
		firstdp=-1
		for j in range(r):
			if img[j,i]==0:
				firstdp=j
				if j>avg:
					valleys.append(i)
				break;
		#print(firstdp)
		#print('\n')
		if firstdp==-1:
			valleys.append(i)
	return valleys,max
def fuzzy(img):
	valleys,max=valley(img)
	for i in range(len(valleys)):
		if valleys

img=cv2.imread('/home/cmater/Rajdeep/handwriting_recognition/data/IAM/words_normalized/trn/a01/a01-000u/a01-000u-00-01.png')
valley(img)



