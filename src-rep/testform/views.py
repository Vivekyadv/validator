import re
from django.shortcuts import render
# from .forms import GeeksForm 


def iphome(request):
    data = request.POST.get('name')
    print(data)
    return render(request, 'validip.html', {'data': data} )

# def home_view(request): 
#     context = {} 
#     form = GeeksForm() 
#     context ['form'] = form 
#     if request.POST:
#     	temp = request.POST['geeks_field']
#     	print(temp)
#     return render( request, "email.html", context) 
