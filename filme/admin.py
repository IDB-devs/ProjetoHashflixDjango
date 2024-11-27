from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin # gerencia os usuarios

# só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets) #para aparecer o campo dos filmes_vistos nos usuarios
campos.append(('Histórico', {'fields': ('filmes_vistos',)}))
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme) #adciona os filmes na pagina do admin
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)