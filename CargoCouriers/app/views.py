from django.shortcuts import render

# Create your views here.
def home(request):
    data_dict = dict()
    data_dict['Navbar'] = 'base/navbar.html'
    return render(request, 'base/base.html', data_dict)

def login(request):
    data_dict = dict()
    data_dict['Navbar'] = 'base/navbar.html'
    data_dict['Data'] = 'forms/login.html'
    return render(request, 'forms/login.html', data_dict)


def signup(request):
    data_dict = dict()
    data_dict['Navbar'] = 'base/navbar.html'
    data_dict['Data'] = 'forms/signup.html'
    return render(request, 'forms/signup.html', data_dict)