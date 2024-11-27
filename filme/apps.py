from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
    
    def ready(self): #criando um superuser para o deploy
        from .models import Usuario
        import os
        
        email = os.getenv('EMAIL_ADMIN') #criar variavel no servidor
        senha = os.getenv('SENHA_ADMIN') #criar variavel no servidor
        
        usuarios = Usuario.objects.filter(email=email)
        if not usuarios: #se a lista estiver vazia
            Usuario.objects.create_superuser(username='admin', email=email, password=senha,
                                             is_active=True, is_staff=True)
