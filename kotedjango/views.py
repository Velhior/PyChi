from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	return render(request, "home_page.html", {})
def about_page(request):
	return render(request, "about_page.html", {})
def contact_page(request):
	if request.method =="POST":
		print(request.POST)
	return render(request, "contact_page.html", {})		