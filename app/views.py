from django.shortcuts import render, redirect
from app.forms import fruitsForm
from app.models import fruits
# Create your views here.
def home(request):
    data = {}
    data['db'] = fruits.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = fruitsForm()
    return render(request, 'form.html', data)

def create(request):
    form = fruitsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = fruits.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = fruits.objects.get(pk=pk)
    data['form'] = fruitsForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = { }
    data['db'] = fruits.objects.get(pk=pk)
    form = fruitsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = fruits.objects.get(pk=pk)
    db.delete()
    return redirect('home')