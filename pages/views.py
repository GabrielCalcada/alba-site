from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'


class sobre(TemplateView):
     template_name='sobre.html'

class praias(TemplateView):
     template_name='praias.html'

class como_chegar(TemplateView):
     template_name='como_chegar.html'

class fale(TemplateView):
     template_name='fale.html'