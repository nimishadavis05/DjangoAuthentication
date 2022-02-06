from django.shortcuts import render,redirect

# Create your views here.
from .forms import CustomUserCreationForm

def Home(request):
	return render(request,"index.html")

def register(request):
	form=CustomUserCreationForm()
	if request.method=='POST':
		form=CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	return render(request,"registration/register.html")

def product_view(request):
	return render(request,"product.html")	