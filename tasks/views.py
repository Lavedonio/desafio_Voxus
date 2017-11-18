# Django imports
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages

# Third party imports
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView

# Tasks app imports
from .models import Task
from .forms import TaskForm


# Função para indicar erros em form
def highlight_error(request, form_list):
    has_error = False
    for form in form_list:
        for field in form:
            if field.errors:
                form.fields[field.name].widget.\
                    attrs['style'] = 'border-color: #EC113F'
                if has_error is False:
                    messages.error(request, "Preencha corretamente os campos "
                                   "obrigatórios")
                has_error = True


# ============================= CRUD Patrocinador ================================
class CreateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('tasks:list')

    # Reescrevo o método abaixo APENAS para guardar o request de post numa
    # variável global, permitindo seu uso em form_valid!
    def post(self, request, *args, **kwargs):
        self.request = request
        return super(CreateTask, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateTask, self).get_context_data(**kwargs)
        context['success_url'] = self.success_url
        return context

    def form_invalid(self, form):
        highlight_error(self.request, [form])
        return super(CreateTask, self).form_invalid(form)


class ListTasks(ListView):
    model = Task
    template_name = "tasks/index.html"
    success_url = reverse_lazy('tasks:list')
    context_object_name = "task_list"

    def get_queryset(self):
        '''Na primeira vez em que se carrega a página, utilizamos o queryset
        default.
        Quando escolhe-se um filtro e clica-se no botão, verificamos o nome
        do filtro, pegamos o correspondente e transformamos o campo
        'filtro_json' em dicionário novamente. Usamos então como argumento do
        método filter().
        '''

        # Pega queryset default
        queryset = super(ListTasks, self).get_queryset()
        return queryset


class EditTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('tasks:list')

    # Reescrevo o método abaixo APENAS para guardar o request de post numa
    # variável global, permitindo seu uso em form_valid!
    def post(self, request, *args, **kwargs):
        self.request = request
        return super(EditTask, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditTask, self).get_context_data(**kwargs)
        context['success_url'] = self.success_url
        return context

    def form_invalid(self, form):
        highlight_error(self.request, [form])
        return super(EditTask, self).form_invalid(form)


class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
