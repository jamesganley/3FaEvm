# -*- coding: utf-8 -*-
"""
@author: jgan
"""

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
y_true = [12, 14, 15, 16, 0]
y_pred = [21, 4, 23, 5 ,0]
confusion_matrix(y_true, y_pred)
y_true = ["authorized"]
y_pred = ["forged"]
confusion_matrix(y_true, y_pred, labels=["forged","authorized"])
tn, fp, fn, tp = confusion_matrix(y_true,y_pred).ravel()
print('true negetive',tn)
print('false positive',fp)
print('false negetive',fn)
print('true posive',tp)
results = confusion_matrix(y_true, y_pred) 
print ('Confusion Matrix :')
print(results) 
print ('Accuracy Score :',accuracy_score(y_true, y_pred) )
print ('Report : ')
print ( classification_report(y_true, y_pred) )