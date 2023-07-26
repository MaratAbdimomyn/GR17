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
    
def update(request):
    if request.method == 'POST':
        four = request.POST.get('update')
        new_name = request.POST.get('name')
        new_country = request.POST.get('country')
        new_driver1 = request.POST.get('driver1')
        new_driver2 = request.POST.get('driver2')
        new_car = request.POST.get('car')
        update_f1teams = Formula1Teams.objects.filter(id = four)
        update_f1teams.update(name=new_name, country=new_country, driver1=new_driver1, driver2=new_driver2, car=new_car)
        return redirect('home')
    else:
        return render(request, 'update.html')
    
def search(request):
    if request.method == 'POST':
        team1 = request.POST.get('search')
        snatch = Formula1Teams.objects.filter(name = team1)
        context = {'snatch':snatch}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')