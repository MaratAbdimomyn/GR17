from django.shortcuts import render, redirect, get_object_or_404
from .models import Formula1Teams

def home(request):
    f1teams = Formula1Teams.objects.all()
    context = {'f1teams':f1teams}
    return render(request, 'home.html', context)

def insert(request):
    if request.method == 'POST':
        one = request.POST
        print(one)
        add_f1teams = Formula1Teams.objects.create(name=one['name'], country=one['country'], driver1=one['driver1'], driver2=one['driver2'], car=one['car'])
        add_f1teams.save()
        return redirect('home')
    else:
        return render(request, 'insert.html')

def delete(request):
    if request.method == 'POST':
        two = request.POST.get('delete')
        Formula1Teams.objects.filter(id = two).delete()
        print(two)
        return redirect('home')
    else:
        return render(request, 'delete.html')