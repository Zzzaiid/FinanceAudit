from django.shortcuts import render, redirect
from .forms import Application_form

def index(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about_us.html')

def clients(request):
    return render(request, 'main/clients.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def news(request):
    return render(request, 'main/news.html')

def zayavka(request):
    error = ''
    if request.method == 'POST':
        form = Application_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно!'
    form = Application_form()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/zayavka.html', data)