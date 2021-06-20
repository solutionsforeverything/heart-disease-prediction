# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import numpy as np

from sklearn.externals import joblib
reloadmodel=joblib.load('./model/lr_file1.pkl')


def index(request):

    context={'a':''}
    return render(request,'index.html',context)
    #return HttpResponse({'a':1})
def second(request):
    context={'a':''}
    return render(request, 'second.html', context)
def predictdisease(request):
    print(request)
    if request.method=='POST':
        temp=[]
        temp.append(request.POST.get('age'))
        temp.append(request.POST.get('sex'))
        temp.append(request.POST.get('cp'))
        temp.append(request.POST.get('trestbps'))
        temp.append(request.POST.get('chol'))
        temp.append(request.POST.get('fbs'))
        temp.append(request.POST.get('restecg'))
        temp.append(request.POST.get('thalach'))
        temp.append(request.POST.get('exang'))
        temp.append(request.POST.get('oldpeak'))
        temp.append(request.POST.get('slope'))
        temp.append(request.POST.get('ca'))
        temp.append(request.POST.get('thal'))
        a=[]
        a.append(temp)
        a= np.array(a, dtype=float)
        scoreval =reloadmodel.predict(a)
        if scoreval==0:
            context={'a':'NO DISESEASE'}
            return render(request, 'second.html', context)
        elif scoreval==1.:
            context={'a':'HAS DISEASE'}
            return render(request, 'second.html', context)