from django.shortcuts import render, redirect, get_object_or_404
from .models import Formula1Teams

def delete(request):
    zero = request.GET
    delete_f1teams = Formula1Teams.objects.delete(id=zero['id'])
    delete_f1teams.save()
    return render(request, 'delete.html')

def delete(request):
    zero = request.GET
    zero = Formula1Teams.objects.get(id=zero['delete'])
    zero.delete()
    return render(request, 'delete.html')

def delete(request):
    zero = request.GET
    print(type(zero))
    return render(request, 'delete.html')

def delete(request):
    zero = request.GET
    Formula1Teams.objects.filter(id = zero['delete']).delete()
    return render(request, 'delete.html')

def delete(request):
    yes = request.GET
    zero = get_object_or_404(Formula1Teams, id=yes['delete'])
    zero.delete()
    return render(request, 'delete.html')