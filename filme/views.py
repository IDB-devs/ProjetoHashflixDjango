from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView #puxando um template do django para criacao de uma class based views
from django.contrib.auth.mixins import LoginRequiredMixin #bloquar paginas para usuarios n logados

#function based views
#Create your views here.
#def homepage(request):
    #return render(request, 'homepage.html')

#class based views
class Homepage(FormView):
    template_name = 'homepage.html' #nome do arquivo html necessario
    form_class = FormHomepage
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario está authenticado
            #redireciona para homefilmes
            return redirect('filme:homefilmes') #redirect('app_name:Path_url_escolhida)
        else:
            return super().get(request, *args, **kwargs) #redireciona para a homepage
        
    def get_success_url(self): #oq fazer qnd o fomulario estiver certo
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


#function based views
# url - view - html
'''def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all() #pegando os filmes do banco de dados
    context['lista_filmes'] = lista_filmes #transformando a lista de filmes em uma variavel para o html
    return render(request, 'homefilmes.html', context)'''
    
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme #object_list sera o nome da lista, lista de filmes do banco de dados
    
    
class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme #object -> 1 item do nosso modelo
    
    def get(self, request, *args, **kwargs):
        #descobrir qual filme o usuario esta visualizando
        filme = self.get_object()
        filme.visualizacoes += 1 # somar nas visualizacoes daquele filme
        filme.save() #salvar no banco de dados
        usuario = request.user
        usuario.filmes_vistos.add(filme) # adcionando a filmes_vistos por esse usuario  
        return super().get(request, *args, **kwargs) #redireciona o usuario para a url final
    
    
    def get_context_data(self, **kwargs): #filmes relacionados
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]#filtrando tabela de filmes pegando os filmes cuja categoria seja igual a categoria do filme da pgina(object)
        context['filmes_relacionados'] = filmes_relacionados
        return context
    

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme
    
    #object_list
    def get_queryset(self): #pesquisa de filmes
        termo_pesquisa = self.request.GET.get('query') #parametro igual o name dele no navbar
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa) #se o titulo contem o termo de pesquisa
            return object_list
        else:
            return None
        

class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario #tabela a ser atualizada
    fields = ['first_name', 'last_name', 'email'] #campos q o usuario podera editar
    
    def get_success_url(self): 
        return reverse('filme:homefilmes')
    
    
class CriarConta(TemplateView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self): #oq fazer qnd o fomulario estiver certo
        return reverse('filme:login') #funcao pede um link (http://www.google.com)