from xml.dom.domreg import registered
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from ml import model as ml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)

#Read the Data
df = pd.read_csv('K:\\ss\\news.csv',index_col=False)
df=df.drop('Unnamed: 0',1)
df.head()
labels = df['label']
x_train, x_test, y_train, y_test = train_test_split(df['text'], labels, test_size = 0.2, random_state = 7)
import pickle
#Initialize a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df = 0.7)

print(type(x_train))
print(x_train)

#Fit and transform train and test set
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
tfidf_test = tfidf_vectorizer.transform(x_test)

# Save the vectorizer
vec_file = 'vectorizer.pickle'
pickle.dump(tfidf_vectorizer, open(vec_file, 'wb'))
pac = PassiveAggressiveClassifier(max_iter = 50)
pac.fit(tfidf_train, y_train)
#Predict on the test set and calculate accuracy
y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(score * 100, 2)}')

# Create your views here.




def complaint(request):
    registered=False
    if request.method=='POST':
        
        form=ComplaintForm(request.POST,request.FILES)
        review=form.data['news']
        sample_text=[review]

        loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
        output_label=pac.predict(loaded_vectorizer.transform(sample_text))
        print(output_label)
        print(review)
        results = output_label
        score = accuracy_score(y_test, y_pred)



        context = {
        'form': form,
        'results': results,
        'prob': score
        }
        return render(request, 'public/review.html', context=context)

    else:
        form=ComplaintForm()   
    context={'registered':registered,'form':form,}
    return render(request,'public/complaint.html',context)

def view_complaints(request):
    c=VerifyNews.objects.all()
    return render(request, 'public/index2.html', {'toi_news':toi_news, 'ht_news': ht_news})



def addcomplaint(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('phoneno') and request.POST.get('complaint'):
                post=complaintss()
                post.name= request.POST.get('name')
                post.phoneno= request.POST.get('phoneno')
                post.complaint= request.POST.get('complaint')
                post.save()
                
                return render(request, 'public/addcomplaint.html')  

    else:
                return render(request,'public/addcomplaint.html')
