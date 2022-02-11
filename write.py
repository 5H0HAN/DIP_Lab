#https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/

import cv2
import os

img = cv2.imread("test.png", cv2.IMREAD_COLOR )
directory = r'/home/theshohan/Desktop/DIP_Lab/output'
os.chdir(directory)

print("Before saving image:")  
print(os.listdir(directory))  

filename = 'savedImage.jpg'


cv2.imwrite(filename, img)


print("After saving image:")  
print(os.listdir(directory))
  
print('Successfully saved')