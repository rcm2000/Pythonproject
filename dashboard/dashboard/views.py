import json
import random
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dashboard.analysis.myanalysis import MyAnalysis


def home(request):
    data = [];
    for i in range(1, 100):
        person = {};
        person['name'] = 'james' + str(i)
        person['position'] = 'position' + str(i)
        person['office'] = 'office' + str(i)
        person['age'] = random.randint(20, 50)
        person['salary'] = str(random.randint(1000, 8000))+'만원'
        dd = time.time()
        person['date'] = time.ctime(dd);
        data.append(person);
    context = {
        'section':'main_section.html',
        'persons': data
    }
    return render(request, 'index.html',context)
def dashboard1(request):
    context = {
        'section':'dashboard1.html'
    };
    return render(request, 'index.html', context)
def dashboard2(request):
    context = {
        'section':'dashboard2.html'
    };
    return render(request, 'index.html', context)
def dashboard3(request):
    context = {
        'section':'dashboard3.html'
    };
    return render(request, 'index.html', context)
def tabledata(request):
    data = [];
    for i in range(1,100):
        person = {};
        person['name'] = 'james' + str(i)
        person['position'] = 'position' + str(i)
        person['office'] = 'office' + str(i)
        person['age'] = random.randint(20,50)
        person['salary'] = random.randint(1000,8000)
        dd = time.time()
        person['date'] = time.ctime(dd);
        data.append(person);

    print(data)
    return HttpResponse(json.dumps(data),content_type='application/json')
def chart1(request):
    data = [{
        'name': 'Tokyo',
        'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
    }, {
        'name': 'London',
        'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
    }]

    return HttpResponse(json.dumps(data),content_type='application/json')

def chart2(request):
    data = [{
        'name': 'Brands',
        'colorByPoint': 'true',
        'data': [{
            'name': 'Chrome',
            'y': 61.41,
            'sliced': 'true',
            'selected': 'true'
        }, {
            'name': 'Internet Explorer',
            'y': 11.84
        }, {
            'name': 'Firefox',
            'y': 10.85
        }, {
            'name': 'Edge',
            'y': 4.67
        }, {
            'name': 'Safari',
            'y': 4.18
        }, {
            'name': 'Sogou Explorer',
            'y': 1.64
        }, {
            'name': 'Opera',
            'y': 1.6
        }, {
            'name': 'QQ',
            'y': 1.2
        }, {
            'name': 'Other',
            'y': 2.61
        }]
    }]

    return HttpResponse(json.dumps(data),content_type='application/json')
def subs(request):
    station = request.GET['station'];
    line = request.GET['line'];
    data = MyAnalysis().subway(station,line);
    return HttpResponse(json.dumps(data),content_type='application/json');
def ages(request):
    target = request.GET['target'];
    data = MyAnalysis().localage(target);
    return HttpResponse(json.dumps(data),content_type='application/json');
def ws(request):
    year = int(request.GET['year']);
    month = int(request.GET['month']);
    data = MyAnalysis().wm(year,month);
    return HttpResponse(json.dumps(data),content_type='application/json');
def genders(request):
    target = request.GET['target'];
    data = MyAnalysis().localage2(target);
    return HttpResponse(json.dumps(data),content_type='application/json');
