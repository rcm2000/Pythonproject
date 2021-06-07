from django.shortcuts import render

from db.DAO.itemdb import ItemDB
from db.DAO.userdb import UserDB
from db.Frame.sqlitedao import Sqlitedao
from db.VO.itemvo import ItemVO
from db.VO.uservo import UserVO

sqlitedao = Sqlitedao('shop')
sqlitedao.makeTable();
udb = UserDB('shop');
idb = ItemDB('shop')

# Create your views here.
def home(request):

    return render(request, 'base.html')
def html5(request):
    context = {
        'section' : 'html5.html',
    };
    return render(request, 'base.html',context)
def css3(request):
    context = {
        'section': 'css3.html',
    };
    return render(request, 'base.html',context)
def javascript(request):
    context = {
        'section': 'javascript.html',
    };
    return render(request, 'base.html',context)
def jquery(request):
    context = {
        'section': 'jquery.html',
    };
    return render(request, 'base.html',context)
def ajax(request):
    context = {
        'section': 'ajax.html',
    };
    return render(request, 'base.html',context)
def register(request):
    context = {
        'section': 'register.html',
    };
    return render(request, 'base.html',context)
def login(request):
    context = {
        'section': 'login.html',
    };
    return render(request, 'base.html',context)
def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    dbuser = udb.select(id);
    name = dbuser.getName()

    context = {};
    try:
        dbuser = udb.select(id);
        if pwd == dbuser.getPwd():
            request.session['sessionid'] = id;
            centerpage = 'loginok.html'
        else:
            raise Exception

    except:
        print('해당하는 아이디나 패스워드가 존재하지 않습니다.')
        centerpage = 'loginfail.html'
    context = {

        'rid': id,
        'section': centerpage,
        'rname' : name
     };

    return render(request, 'base.html',context)
def regimpl(request):
    id = request.GET['id'];
    pwd = request.GET['pwd'];
    name = request.GET['name'];
    user = UserVO(id,pwd,name);
    udb.insert(user);
    context = {
        'section': 'registerok.html',
        'rname': name,
        'rid': id
    };
    return render(request, 'base.html',context)
def logout(request):
    if request.session['sessionid'] != None:
        del request.session['sessionid'];
    return render(request, 'base.html')
def userlist(request):
    users = udb.selectall();
    context = {
        #selectall로 db에 있는 모든 사용자 정보를 불러 들인다.
        #id 와 이름만 따로 불러내 저장하고 반복문을 이용하여 개시한다.
        'userlist' : users,
        'section': 'userlist.html',
    };
    return render(request, 'base.html',context)
def additem(request):
    context = {
        'section': 'additem.html',
    };
    return render(request, 'base.html',context)
def itemlist(request):
    context = {
        'section': 'itemlist.html',
    };
    return render(request, 'base.html',context)
def itemimpl(request):
    name = request.POST['name'];
    price = request.POST['price'];
    item = ItemVO('id',name, price,'date');
    udb.insert(item);


    context = {
        'section': 'itemok.html',
        'rname': name,

    };
    # try:
    #     dbitem = idb.select(id);
    #     if item != dbitem.getName():
    #         request.session['sessionitem'] = item;
    #         centerpage = 'itmeok.html'
    #     else:
    #         raise Exception
    #
    # except:
    #     print('중복되는 아이템이 존제합니다.')
    #     centerpage = 'itemfail.html'
    # context = {
    #     'rid': id,
    #     'section': centerpage,
    #
    #  };

    return render(request, 'base.html',context)

