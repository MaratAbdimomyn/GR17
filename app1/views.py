from django.shortcuts import render, redirect
from .models import Formula1Teams

def home(request):
    f1teams = Formula1Teams.objects.all()
    context = {'f1teams':f1teams}
    return render(request, 'home.html', context)

def insert(request):
    if request.method == 'POST':
        data = request.POST
        add_f1teams = Formula1Teams.objects.create(name=data['name'], country=data['country'], driver1=data['driver1'], driver2=data['driver2'], car=data['car'])
        add_f1teams.save()
        return redirect('home')
    else:
        return render(request, 'insert.html')