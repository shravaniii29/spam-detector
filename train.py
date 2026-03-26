# train.py — Spam Detection Model Trainer

import os
import pickle
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print('Step 1: Loading dataset...')

categories = ['talk.politics.misc', 'sci.space']
data = fetch_20newsgroups(subset='all', categories=categories,
                          remove=('headers', 'footers', 'quotes'))

X = data.data
y = data.target

print('Step 2: Splitting data...')
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print('Step 3: Vectorizing text...')
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print('Step 4: Training model...')
model = MultinomialNB()
model.fit(X_train_vec, y_train)

print('Step 5: Evaluating...')
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%')

print('Step 6: Saving model...')
os.makedirs('model', exist_ok=True)

with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print('SUCCESS: Model saved!')