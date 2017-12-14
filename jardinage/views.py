from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
class JardinList(ListView):
    model = jardin
    template_name = "jardin_list.html"
    context_object_name = "garden"


class JardinCreate(CreateView):
    model = jardin
    fields = ['nom', 'adresse', 'ville']
    template_name = "jardin_create.html"
    context_object_name = "garden"
    success_url = reverse_lazy('jardin')

    def get_absolute_url(self):
        return reverse('jardin')


class JardinUpdate(UpdateView):
    model = jardin
    fields = ['nom', 'adresse', 'ville']
    template_name = "jardin_update.html"
    context_object_name = "garden"
    success_url = reverse_lazy('jardin')


class JardinDelete(DeleteView):
    model = jardin
    template_name = "jardin_delete.html"
    success_url = reverse_lazy('jardin')


#--------------------------------Plante------------------------------------------

class PlanteList(ListView):
    model = plante
    template_name = "plante_list.html"
    context_object_name = "garden"
    liste = plante.objects.distinct('id_jardin')

    #test pour sourcetree
    vxgfxwfdwfvxfdwfdwrdd


class PlanteCreate(CreateView):
    model = plante
    fields = ['nom', 'date_naissance', 'date_deces', 'id_variete', 'id_jardin']
    template_name = "plante_create.html"
    context_object_name = "garden"
    success_url = reverse_lazy('plante')


class PlanteUpdate(UpdateView):
    model = plante
    fields = ['nom', 'date_naissance', 'date_deces', 'id_variete', 'id_jardin']
    template_name = "plante_update.html"
    context_object_name = "garden"
    success_url = reverse_lazy('plante')


class PlanteDelete(DeleteView):
    model = plante
    template_name = "plante_delete.html"
    success_url = reverse_lazy('plante')


#--------------------------------Variete------------------------------------------

class VarieteList(ListView):
    model = variete
    template_name = "variete_list.html"
    context_object_name = "garden"


class VarieteCreate(CreateView):
    model = variete
    fields = ['nom']
    template_name = "variete_create.html"
    context_object_name = "garden"
    success_url = reverse_lazy('variete')


class VarieteUpdate(UpdateView):
    model = variete
    fields = ['nom']
    template_name = "variete_update.html"
    context_object_name = "garden"
    success_url = reverse_lazy('variete')


class VarieteDelete(DeleteView):
    model = variete
    template_name = "variete_delete.html"
    success_url = reverse_lazy('variete')
