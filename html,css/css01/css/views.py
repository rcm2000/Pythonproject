from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'css08.html')
def html5(request):
    centext = {
        'section':'html5.html',
    };
    return render(request, 'html5.html')
def css3(request):
    centext = {
        'section': 'css3.html',
    }
    return render(request, 'css08.html')
def javascript(request):

    return render(request, 'css08.html')
def ajax(request):

    return render(request, 'css08.html')
