from django.urls import path
from .views import HomePageView, sobre, praias, como_chegar, fale


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('Sobre/', sobre.as_view(), name='sobre'),
    path('Praias/', praias.as_view(), name='praias'),
    path('Como_chegar/', como_chegar.as_view(), name='como_chegar'),
    path('Fale/', fale.as_view(), name='fale'),
    # path('sobre/', sobre.as_view(), name='sobre')
]