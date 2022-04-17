from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegisterUserForm

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class FindGame(TemplateView):
    template_name = 'findgame.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        zip = self.request.GET.get("zip")
        if zip != None:
            context["games"] = Game.objects.filter(zip__icontains=zip)
            context["header"] = f"Searching for games near {zip}" 
        else:
            context['games'] = Game.objects.all()
            context['header'] = 'All Games'
        return context

@method_decorator(login_required, name='dispatch')
class CreateGame(CreateView):
    model = Game
    fields = ['title', 'game_type', 'time', 'date', 'street', 'city', 'state', 'zip', 'img']
    template_name = 'creategame.html'
    def get_success_url(self):
        return reverse('gamedetail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.object.user
        self.object.save()

        return HttpResponseRedirect('/findgame/')

class GameDetail(DetailView):
    model = Game
    template_name = 'gamedetail.html'

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    game = Game.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'game': game})

def signup_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})    
    else:
        form = RegisterUserForm()
        return render(request, 'signup.html', {'form': form})

