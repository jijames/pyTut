# Image similarity using perceptual hashing
# pip install imagehash PIL
# Quick and dirty perceptual hashing:
# https://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
# https://github.com/bjlittle/imagehash

from PIL import Image
import imagehash
import sys, os

# Take in two images from the command line and calculate their hash
#h1 = imagehash.average_hash(Image.open(sys.argv[1]))
#h2 = imagehash.average_hash(Image.open(sys.argv[2]))
#print(h1)
#print(h2)
# Subtract their hash values to get a similarity score
#print(h1 - h2)

# Assignment 4
# Accept either 2 images or a single directory
# If two images, compare their phash values
# If a directory, compare each file in the directory with every other file

# Image classification requirements
# pip install scikit-learn
# pip install matplotlib

# sklearn is scikit-learn and has our ML algorithms
import sklearn
from numpy import array

#dataSet = []
#img = Image.open(sys.argv[1])
#img = img.convert('L')
#arr = array(img)
#print(arr)

# Lets look at the features
#from pylab import *
#figure()
#gray()
#contour(arr, origin='image')
#axis('equal')
#axis('off')
#figure()
#hist(arr.flatten(), 128)
#show()

# We need to convert our images into a numpy array type.
# Features are extracted from an image and represented as numpy array
import numpy as np
# A support vector machine is a common machine learning alg.
from sklearn import svm
# This is used to test our models accuracy
from sklearn.model_selection import train_test_split
# Lets learn features from all cats and dogs
# Xlist is a holder for the features as an np array
#Xlist=[]
# Ylist is a holder for our labels (dog or cat)
#Ylist=[]
#for root, dirs, files in os.walk("corpus"):
#    flabel = root[-4:] # This works because dogs and cats are both 4 chars
#    for name in files:
#        print(os.path.join(root, name))
        # Here we use python image library to open the image
#        img = Image.open(os.path.join(root, name))
        # Convert the image to greyscale
#        img = img.convert('L')
        # Convert to numpy array
#        featurevector=np.array(img).flatten()[:50]
        # Add features to xlist
#        Xlist.append(featurevector)
        # Add lables to y list
#        Ylist.append(flabel)
# Extract a training and test sets from our data set
#X_train, X_test, y_train, y_test = train_test_split(
#     Xlist, Ylist, test_size=0.4, random_state=1)
# Train an SVM classifier on our data set
#clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# Test the trained model with our test data set
#print("SVM: " + str(clf.score(X_test, y_test)))

# Assignment 5
# Adjust the SVM options to try to improve the classificaiton rate
# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
