from django.shortcuts import render

# Create your views here.
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