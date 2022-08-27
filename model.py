import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib


df = pd.read_csv("clickbait_data.csv", encoding="latin-1")
x = df["headline"]
y = df["clickbait"]

# Check
# print(df)

#Create countVectorizer
cv = CountVectorizer()

#fit_transform requires an iterable which generates either str, unicode or file objects
# as input. 
# Apparently, <class 'pandas.core.series.Series'> from x = df["message"]
# satisfies this condition

#fit_transform does two things: 
# Found all of the different words in the text
# Counted how many of each there were
# array of shape (n_samples, n_features)
# Document-term matrix.

X = cv.fit_transform(x)

# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
# Split arrays or matrices into random train and test subsets
# sklearn.model_selection.train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Prediction method: Multinomial Naive Bayes
# Already performs Laplace Smoothing as default
clf = MultinomialNB()

# Trains model on training data
clf.fit(X_train,y_train)

# Returns float of correct predictions/all predictions for info
print(clf.score(X_test,y_test))

# Predict on test data
y_pred = clf.predict(X_test)

# Evaluate predictions on test data
print(classification_report(y_test, y_pred))

# Save model as .pkl file for later use: “persist model in a standard format”
# that is, models are persisted in a certain format specific to the language 
# in development.
joblib.dump(clf, 'clickbait_model.pkl')
joblib.dump(cv, "cv_vocab.pkl")

# Syntax to load model back:
# NB_spam_model = open('NB_spam_model.pkl','rb')
# clf = joblib.load(NB_spam_model)

