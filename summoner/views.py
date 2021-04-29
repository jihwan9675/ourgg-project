from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import SummonerForm

class SummonerView(FormView):
    template_name = 'summoner.html'
    form_class = SummonerForm