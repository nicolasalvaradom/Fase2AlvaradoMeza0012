from django.shortcuts import render
from django.views import generic
from .models import Game, Genre

# Create your views here.
def index(request):
    num_games=Game.objects.all()

    return render(
        request,
        'index.html',
        context={'num_games':num_games},
    )

def games(request):
    num_games=Game.objects.all()

    return render(
        request,
        'index.html',
        context={'num_games':num_games},
    )

def noticias(request):
    return render(
        request,
        'noticias.html',
    )

def quienessomos(request):

     return render(
        request,
        'quienessomos.html',
    )

def store(request):

     return render(
        request,
        'store.html',
    )

def formulario(request):
     return render(
        request,
        'formulario.html',
    )

def confirmacion(request):
     return render(
        request,
        'confirmacion.html',
    )

class GameListView(generic.ListView):
    model = Game
    paginate_by = 10
class GameDetailView(generic.DetailView):
    model = Game