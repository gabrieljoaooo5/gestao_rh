from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from ..documento.models import Documento
from ..registro_hora_extra.models import RegistroHoraExtra


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def get_context_data(self, **kwargs):
        context = super(FuncionarioEdit, self).get_context_data(**kwargs)
        context.update({'documentos': Documento.objects.filter(pertence__id=self.kwargs['pk']),
                        'banco_horas': RegistroHoraExtra.objects.filter(funcionario__id=self.kwargs['pk'])})
        return context


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username=username,
        )
        funcionario.save()

        return super(FuncionarioNovo, self).form_valid(form)
