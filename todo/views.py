from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import List
from django.contrib import messages
from .forms import ListForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added successfully'))
            return render(request, 'home.html', {'all_items':all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ('Item has been deleted successfully'))
    return redirect('home')

def done(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('home')

def undone(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited successfully'))
            return redirect('home')

    else:
        item = List.objects.get(pk = list_id)
        return render(request, 'edit.html', {'item':item})
    
