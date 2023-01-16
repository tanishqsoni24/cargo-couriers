from django.shortcuts import render

# Create your views here.
def home(request):
    data_dict = dict()
    data_dict['Navbar'] = 'base/navbar.html'
    return render(request, 'base/base.html', data_dict)