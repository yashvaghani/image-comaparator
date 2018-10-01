# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from resize import image_resize
from loop import fpath

def compare_images(imageA, imageB, title):
    m=mse(imageA,imageB)
    s=ssim(imageA,imageB)
    fig=plt.figure(title)
    plt.suptitle("MSE: %.2f,  SSIM: %.2f "%(m,s))
    if s>0.93:
        print("mse and accuracy:",m,s)
        ax=fig.add_subplot(1,2,1)
        plt.imshow(imageA,cmap=plt.cm.gray)
        plt.axis("off")
        ax=fig.add_subplot(1,2,2)
        plt.imshow(imageB,cmap=plt.cm.gray)
        plt.axis("off")
        plt.show()
        return 1
    else:                       #C:\Users\yashv\Documents    C:\Users\yashv\Documents\Python Scripts
        return 0

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err
a=input("enter path 1:")
b=input("enter path 2:")
l1=[]
l2=[]                  # C:\Users\yashv    C:\Users\yashv\Documents
l1=fpath(a)
l2=fpath(b)    
j=0
i=0
for i in range(len(l1)):
    for j in range(len(l2)):
        source1 = cv2.imread(l1[i]) #C:\Users\yashv\Documents\Python Scripts  E:\aa
        source2 = cv2.imread(l2[j])
        h,w,c=source1.shape
        h1,w1,c1=source2.shape
        '''print(source1.shape)
        print(source2.shape)'''
        if(h!=h1 and w!=w1 and (h*w)!=(h1*w1)):
            if((h*w)<(h1*w1)):
                source2=image_resize(source2,w,h)
                #print("after of source 2",source2.shape)
            elif((h*w)>(h1*w1)):
                source1=image_resize(source1,w1,h1)
                #print("after of source 1",source1.shape)
        source1 = cv2.cvtColor(source1, cv2.COLOR_BGR2GRAY)
        source2 = cv2.cvtColor(source2, cv2.COLOR_BGR2GRAY)
        d=compare_images(source1,source2, "a")
        if d==1:
            print ("path1:",l1[i],"and    path 2: ",l2[j])
            
        
        
