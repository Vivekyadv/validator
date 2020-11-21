from django.shortcuts import render


def home(request, *args, **kwargs):
	return render(request,'blog/home.html')

def ip(request, *args, **kwargs):
	return render (request, 'blog/ip.html')

def mac(request, *args, **kwargs):
	return render (request, 'blog/mac.html')