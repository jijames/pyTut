# For machine learning tasks, we need a lot of data. We also need to
# prepare the data in a format that answers our questions, and is supported
# by the learning system. When dealing with very large amounts of data
# you should also consider efficiency and memory.

# SMS Dataset from:
# http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/
# First, lets use the NLTK and textblob to classify tagged data.

#pip install nltk
#pip install textblob
# python -m textblob.download_corpora

# Random to randomize our data set
import random
import os, csv
# Textblob is a library that helps with text analysis
from textblob.classifiers import NaiveBayesClassifier

# The data we want to learn something about is in SMSSpamCollection.txt
#with open("corpus/SMSSpamCollection.txt") as f:
#    corpus = f.readlines()
    # Get the data and shuffle so we have a different set each time
#    random.shuffle(corpus)
    # Save the data in a CSV file type
#    with open("data.tmp", "a") as fn:
        # First write the col titles
#        fn.write("Text,Label\n\r")
        # Use i and enumerate to keep track of the number of loops
#        for i, line in enumerate(corpus):
            # Stop the loop after 200 to limit our data set (faster)
#            if i > 200:
#                break
#            else:
#                tag,text = line.split("\t")
                #print("The tag is: " + tag)
#                if tag and text:  # if not empty, write the data
#                    fn.write(text.strip("\n\r").replace(",", "") + "," + tag + "\n\r")
#    fn.close()
#f.close()

#trainingSet = []
# Open the training set csv
#with open("data.tmp", "r") as csvData:
#    reader = csv.DictReader(csvData)
#    for row in reader:
        # Save the csv data as a hashtable
#        trainingSet.append((row['Text'], row['Label']))

#print(trainingSet)
# Use textblob Bayes Classifier
# https://textblob.readthedocs.io/en/dev/classifiers.html
#cl = NaiveBayesClassifier(trainingSet)
# Print the most important features
#print(cl.show_informative_features(5))
# Try classifying some text based on our model
#print(cl.classify("You are amazing!"))
#print(cl.classify("Buy our stuff now!"))

# Look at the probability distribution of the classification
#probDist = cl.prob_classify("Call me a taco.")
#print("Ham score: " + str(round(probDist.prob("ham"),2)))
#print("Spam score: " + str(round(probDist.prob("spam"),2)))

#os.remove("data.tmp")

# Lesson 3 Assignment
# Convert emails in the corpus folder to CSV and classify using textblob
