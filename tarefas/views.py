from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    if request.method == 'POST':
        texto = request.POST.get('tarefa')
        Tarefa.objects.create(tarefa=texto)
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

