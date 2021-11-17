from django.shortcuts import render, redirect
from .models import Users
from .form import UserForm

def user_list(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, "crud/crud_list.html", context)

def user_form(request, email=''):
    if request.method == "GET":
        if email == '':
            form = UserForm()
        else:
            user = Users.objects.get(pk=email)
            form = UserForm(instance=user)
        return render(request, "crud/crud_form.html", {'form': form})
    else:
        if email == '':
            form = UserForm(request.POST)
        else:
            user = Users.objects.get(pk=email)
            form = UserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
        return redirect('/list')

def user_delete(request, email):
    user = Users.objects.get(pk=email)
    user.delete()
    return redirect('/list')



