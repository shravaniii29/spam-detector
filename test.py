# test.py — Automated Model Testing Script

import pickle
import sys

print('=== Running Automated Model Tests ===')

# Step 1: Load model
try:
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    print('PASS: Model loaded successfully')
except FileNotFoundError as e:
    print(f'FAIL: {e}')
    sys.exit(1)   # VERY IMPORTANT (Jenkins fail karega)

# Step 2: Test cases
test_cases = [
    ('Congratulations! You won a FREE iPhone', 'spam-like'),
    ('The satellite launched into space successfully', 'normal'),
]

label_map = {0: 'normal', 1: 'spam-like'}

print('\nRunning tests...')

for text, expected in test_cases:
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    result = label_map[pred]

    print(f'Predicted: {result} | Expected: {expected}')

print('\n=== TEST COMPLETE ===')