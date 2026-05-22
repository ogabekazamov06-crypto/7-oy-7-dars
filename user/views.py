from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,User,AuthenticationForm
from django.contrib import messages


def registr_view(request):
    if request.method == 'POST':
        form =RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Hisob yaxshi ochildi ota")
            return redirect('course_list')
    else:
        form = RegisterForm()
    context = {
              'form': form
            }
    return render(request, 'user/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, "hisobga yaxshi kirildi!!")
            return  redirect('course_list')
    else:
        form = AuthenticationForm()
    context ={
        'form': form
    }
    return render(request, 'user/register.html', context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.warning(request, 'Tizimdan yaxshi chiqib ketdingiz')
    return redirect('login')




