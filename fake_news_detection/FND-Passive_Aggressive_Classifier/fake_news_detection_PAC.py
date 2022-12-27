#Make necessary import
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#Read the data

#Now, let’s read the data into a DataFrame, and get the shape of the data and the first 5 records.
data_frame=pd.read_csv('data/news.csv')

#Get shape
data_frame.shape

#Get shape and head
print(data_frame.columns)

#after ru in spyder console run data_frame.head()

#Get the labels

#And get the labels from the DataFrame.
labels = data_frame.label
labels.head()

#Split the dataset

#Split the dataset into training and testing sets.
x_train,x_test,y_train,y_test=train_test_split(data_frame['text'], labels, test_size=0.2, random_state=7)


#Initialize a TfidfVectorizer

"""Let’s initialize a TfidfVectorizer with stop words from the English language and a maximum document 
frequency of 0.7 (terms with a higher document frequency will be discarded). Stop words are the most common 
words in a language that are to be filtered out before processing the natural language data. And a TfidfVectorizer 
turns a collection of raw documents into a matrix of TF-IDF features."""
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

#Fit and transform train set, transform test set
#Now, fit and transform the vectorizer on the train set, and transform the vectorizer on the test set.
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)


#Initialize a PassiveAggressiveClassifier
#Next, we’ll initialize a PassiveAggressiveClassifier. This is. We’ll fit this on tfidf_train and y_train.
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

#Predict on the test set and calculate accuracy
"""Then, we’ll predict on the test set from the TfidfVectorizer and calculate the accuracy 
with accuracy_score() from sklearn.metrics."""
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

#Output: Accuracy: 93.13%

#DBuild confusion matrix
"""We got an accuracy of 92.82% with this model. Finally, let’s print out a confusion matrix to gain insight 
into the number of false and true negatives and positives."""
confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])

"""output:
    array([[590,  48],
          [ 39, 590]])"""
#So with this model, we have 590 true positives, 590 true negatives, 39 false positives, and 48 false negatives.

