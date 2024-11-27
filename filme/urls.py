from django.urls import path, reverse_lazy
from .views import Homefilmes, Homepage, Detalhesfilme, PesquisaFilme, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_view

#sempre q for construir uma pagina precisa (url(link) - view(oq vai acontecer qnd tentar acessar a pagina) - template(oq a pagina exibe))

app_name = 'filme' #namespace url hashflix

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'), #view
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'), #path diferente pra cada filme, inteiro:primary key -> banco de dados
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', PaginaPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', #utilizando pagina ja existente editada
                                                             success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]

