from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    if request.method == 'POST':
        texto = request.POST.get('tarefa')
        Tarefa.objects.create(tarefa=texto)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def concluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')


