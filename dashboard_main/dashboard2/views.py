from django.shortcuts import render

# Create your views here.
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