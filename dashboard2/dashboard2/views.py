import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis.Myanalysis import myanalysis, Titanic, Open, Naver


def home(request):
	context = {
		'section': 'main_center.html',
	}
	return render(request, 'index.html', context)
def d1(request):
	context = {
		'section': 'd1.html',
	}
	return render(request, 'index.html', context)
def d2(request):
	context = {
		'section': 'd2.html',
	}
	return render(request, 'index.html', context)
def d3(request):
	context = {
		'section': 'd3.html',
	}
	return render(request, 'index.html', context)
def d4(request):
	context = {
		'section': 'd4.html',
	}
	return render(request, 'index.html', context)
def d5(request):
	context = {
		'section': 'd5.html',
	}
	return render(request, 'index.html', context)
def geo(request):
	context = {
		'section': 'geo.html',
	}
	return render(request, 'index.html', context)
def acc(request):
	year = request.GET['year'];
	sido = request.GET['sido'];
	gungu = request.GET['gungu'];
	data = myanalysis().d1(year,sido,gungu);
	return HttpResponse(json.dumps(data),content_type='application/json');
def d1s(request):
	option = request.GET['option'];
	data = Titanic().t1(option);
	return HttpResponse(json.dumps(data),content_type='application/json');
def d3s(request):
	startdt = request.GET['startdt'];
	enddt = request.GET['enddt'];
	data = Open().o1(startdt,enddt);
	print(data)
	return HttpResponse(json.dumps(data),content_type='application/json');
def d4s(request):
	data = Naver().n1();
	return HttpResponse(json.dumps(data),content_type='application/json');
