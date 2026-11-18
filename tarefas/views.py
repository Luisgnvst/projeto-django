from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    if request.method == 'POST':
        texto = request.POST.get('tarefa')
        Tarefa.objects.create(tarefa=texto)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})


