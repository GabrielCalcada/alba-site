from django.urls import path
from .views import HomePageView
from .views import sobre
from .views import praias
from .views import como_chegar
from .views import fale

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('Sobre/', sobre.as_view(), name='sobre'),
    path('Praias/', praias.as_view(), name='praias'),
    path('Como-chegar/', como_chegar.as_view(), name='como_chegar'),
    path('Fale/', fale.as_view(), name='fale'),
    # path('sobre/', sobre.as_view(), name='sobre')
]