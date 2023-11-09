from django.http import HttpResponse
from django.shortcuts import render

from app10.models import Anceta


# Create your views here.
def start_page(request):
    context = {'ancetas': Anceta.objects.all()}

    return render(request,'index.html', context)

def create_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        login = request.POST.get('login')
        password = request.POST.get('password')
        age = request.POST.get('age')
        hobbies = request.POST.get('hobbies')
        favourite_mosics = request.POST.get('favourite_mosics')
        favourite_movies = request.POST.get('favourite_movies')
        favourite_books = request.POST.get('favourite_books')
        favourite_anime = request.POST.get('favourite_anime')

        anceta = Anceta(name=name, surname=surname, login=login, password=password, age=age, hobbies=hobbies, favourite_mosics=favourite_mosics, favourite_movies=favourite_movies, favourite_books=favourite_books, favourite_anime=favourite_anime)
        anceta.save()

    return render(request,'create_profil.html')




def detail_page(request, pk):
    context = {'detail':Anceta.objects.get(pk=pk)}
    return render(request, 'profile_detail.html', context)