from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
	return render(request, "home_page.html", {})
def about_page(request):
	return render(request, "about_page.html", {})
def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"form" : contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method =="POST":
	# 	print(request.POST)
	return render(request, "contact_page.html", context)		