# Importações do Django
from django.contrib import admin

# Importações do Projeto
from .models import *


class TaskAdmin(admin.ModelAdmin):
    """Esta classe edita a página que lista os objetos da classe Post no admin,
    tornando mais fácil a visualização e edição.
    Para mais informações sobre as opções de visualização,
    visite: https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#modeladmin-options"""

    class Meta:
        # Linka esta classe do Admin com a classe do Models abaixo
        model = Task

    # Mostram esses campos na lista de objetos da classe
    list_display = ["name", "description", "priority"]

    # Coloca o campo como clicável
    list_display_links = ["name"]

    # Adiciona filtro nos campos
    list_filter = ["name", "priority"]

    # Torna os campos pesquisáveis
    search_fields = ["name", "contato"]

    # Torna o campo editável
    # list_editable = ["description"]


# Sem essa linha, a classe Patrocinador não aparece no admin
admin.site.register(Task, TaskAdmin)
