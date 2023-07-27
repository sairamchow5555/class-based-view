from django.shortcuts import render
from testapp.models import Beer
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class BeerListView(ListView):
    model = Beer
    #d_t_f = beer_list.html
    #d_c_o = beer_list

class BeerDetailView(DetailView):
    model = Beer
    #d_t_f = beer_detail.html
    #d_c_o = beer or object

class BeerCreateView(CreateView):
    model = Beer
    fields = '__all__'
    #d_t_f = beer_form.html

class BeerUpdateView(UpdateView):
    model = Beer
    fields = '__all__'
    #d_t_f = beer_form.html

from django.urls import reverse_lazy
class BeerDeleteView(DeleteView):
    model = Beer
    #d_t_f = beer_confirm_delete.html
    success_url = reverse_lazy('list')
