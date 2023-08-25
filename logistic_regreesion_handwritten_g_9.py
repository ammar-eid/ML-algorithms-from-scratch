# -*- coding: utf-8 -*-
"""Copy of Logistic_Regreesion_handWritten G 9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ianHWDPCtqLHPLrqa-FW70LDdrpNm4Pd
"""

from sklearn.datasets import load_digits
digits = load_digits()

import matplotlib.pyplot as plt
for i in range(3):
   plt.matshow(digits.images[i])

digits.target_names

#dir() function returns all properties and methods of the specified object, without the values.
dir(digits)

digits.data[0]

# Print to show there are 1797 images (8 by 8 images for a dimensionality of 64)
print("Image Data Shape" , digits.data.shape)
# Print to show there are 1797 labels (integers from 0–9)
#print("Label Data Shape", digits.target.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25)

'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)'''

from sklearn.linear_model import LogisticRegression
# all parameters not specified are set to their defaults
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

y_prd=logisticRegr.predict(x_test)

#from sklearn import metrics , accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_prd)
print(cm)

acc = accuracy_score(y_test, y_prd)
acc

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')