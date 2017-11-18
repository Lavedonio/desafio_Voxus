# Importações do Django
from django.conf.urls import url

# Importações do Projeto
from . import views

urlpatterns = [
    # A url deve serguir o segunte modelo:
    # url(r'^[Nome da URL]/$', views.[Nome da Função da Views].as_view(), name="[Nome da URL para ser chamada no código]"),

    url(r'^$', views.ListTasks.as_view(), name='list'),
    url(r'^create/$', views.CreateTask.as_view(), name='create'),

    # O (?P<id>\d+) no URL serve para passar números apenas.
    # O nome entre < > (no caso, "id") deve ser o mesmo do parâmetro da função da views correspondente.
    url(r'^(?P<id>\d+)/edit/$', views.EditTask.as_view(), name='edit'),
    url(r'^(?P<id>\d+)/delete/$', views.DeleteTask.as_view(), name='delete'),
]
