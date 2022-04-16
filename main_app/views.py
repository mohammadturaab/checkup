from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse

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

