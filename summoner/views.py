from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import SummonerForm

class SummonerView(FormView):
    template_name = 'summoner.html'
    form_class = SummonerForm

    def get(self, request, *args, **kwargs):  # GET Method (preidct/)
        #print(request.GET['userName'])
        pass
        
        form = self.form_class(request, initial=self.initial)
        return render(request, self.template_name, {'form': form, 'username': request.session.get('user')})