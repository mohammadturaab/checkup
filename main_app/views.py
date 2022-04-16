from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Game

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

