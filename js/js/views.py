import json
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from data.adata import Adata
from data.tempa import Tempa


def home(request):

    return render(request, 'home.html')
def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    return render(request, 'jq04.html');
def regimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    age = request.POST['age'];
    context = {
        'rname': name,
        'rid': id,
        'rpwd': pwd,
        'rage': age
    };
    return render(request, 'registerok.html',context);

def ajs01(request):
    now = time.time()
    return HttpResponse(time.ctime(now));

def ajs011(request):
    data = Adata().aj011();

    return HttpResponse(json.dumps(data),content_type='application/json');

def ajs02(request):
    cmd = request.GET['cmd'];
    data = Adata().aj02(cmd)
    return HttpResponse(json.dumps(data),content_type='application/json');
def ajs03(request):
    cmd = request.GET['cmd'];
    data = Adata().aj03(cmd);
    return HttpResponse(json.dumps(data),content_type='application/json');
def ajs04(request):
    year = int(request.GET['year']);
    month = int(request.GET['month']);
    cmd = request.GET['cmd'];
    data = Tempa().aj04(year,month,cmd);
    return HttpResponse(json.dumps(data),content_type='application/json');
def ajs05(request):
    data = Tempa().aj05();
    return HttpResponse(json.dumps(data),content_type='application/json');
def ajs06(request):
    year = int(request.GET['year']);
    cmd = request.GET['cmd'];
    data = Tempa().aj06(year,cmd);
    return HttpResponse(json.dumps(data),content_type='application/json');