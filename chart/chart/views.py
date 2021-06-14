import json
import logging
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from chart.analysis.myanalysis import MyAnalysis

user_logger = logging.getLogger('users');
item_logger = logging.getLogger('items');
iot_logger = logging.getLogger('iot_file');

def home(request):

    return render(request, 'home.html')
def ws(request):
    year = int(request.GET['year']);
    month = int(request.GET['month']);
    data = MyAnalysis().wm(year,month);
    return HttpResponse(json.dumps(data),content_type='application/json');
def ages(request):
    target = request.GET['target'];
    data = MyAnalysis().localage(target);
    return HttpResponse(json.dumps(data),content_type='application/json');
def genders(request):
    target = request.GET['target'];
    data = MyAnalysis().localage2(target);
    return HttpResponse(json.dumps(data),content_type='application/json');
def pers(request):
    target = request.GET['target'];
    data = MyAnalysis().localage3(target);
    return HttpResponse(json.dumps(data),content_type='application/json');
def subs(request):
    station = request.GET['station'];
    line = request.GET['line'];
    data = MyAnalysis().subway(station,line);
    return HttpResponse(json.dumps(data),content_type='application/json');
def iots(request):
    speed = request.GET['speed'];
    rpm = request.GET['rpm'];
    temp = request.GET['temp'];
    t = time.localtime()
    now = str(t.tm_year)+'-'+str(t.tm_mon)+'-'+str(t.tm_mday)+' '+str(t.tm_hour)+':'+str(t.tm_min)
    iot_logger.debug(speed+','+rpm+','+temp);
    #print(now,speed,rpm,temp);
    return render(request, 'ok.html')
