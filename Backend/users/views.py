from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm


#funções que vão responder a request
def list_users(request):
    #acesso lista do banco e retorno ao navegador
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def create_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')
    return render(request, 'users-form.html', {'form': form})


def  update_user(request,id):
    user = get_object_or_404(users, pk=id)
    form = UserForm(request.POST or None, instance=users)

    if form.is_valid():
        form.save()
        return redirect('list_users')
    return render(request, 'users-form.html', {'form': form})


def  delete_user(request, id):
    user = get_object_or_404(users, pk=id)
    form = UserForm(request.POST or None, instance = users)
    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    return render(request, 'user-delete-confirm.html', {'form':form, 'users': users})
