import numpy as np
import pandas as pd
import os
import pickle
from .store import getsymptoms, getDiseases, getReplaceDict
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
l1= getsymptoms()

disease= getDiseases()

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

path = r'D:\\all files\\programming practice\\web\\website\\predict\\'
print(path)

def NaiveBayes(symptoms):
    
    psymptoms = symptoms
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    model = pickle.load(open('Naive.sav', 'rb'))
    predict = model.predict(inputtest)
    predicted=predict[0]


    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break
    
    if (h == 'no'):
        return "Not sufficient data"
    if (h=='yes'):
        return disease[a]
    else:
        return "No Disease"
        
def randomforest(symptoms):
    psymptoms = symptoms
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    model = pickle.load(open('randomforest.sav', 'rb'))
    predict = model.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        return disease[a]
    else:
        return "No Disease"


def functionSVM(symptoms):
    psymptoms = symptoms
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    model = pickle.load(open('svm.sav', 'rb'))
    predictions = model.predict(inputtest) 
    return predictions[0]


def runApp(symptoms = ['sweating','dehydration','blood_in_sputum','family_history','high_fever']):
    dis = []
    dis.append(NaiveBayes(symptoms))
    dis.append(randomforest(symptoms))
    dis.append(functionSVM(symptoms))
    return dis