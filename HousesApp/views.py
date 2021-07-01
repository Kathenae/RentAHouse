from .models import HouseListing

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "HousesApp/houses_home.html"

class HousesListView(ListView):
    model = HouseListing
    context_object_name = "houses"
    template_name = "HousesApp/houses_list.html"

class HouseDetailView(DetailView):
    model = HouseListing
    context_object_name = "house"
    template_name = "HousesApp/houses_details.html"

class HouseCreateView(LoginRequiredMixin,CreateView):
    model = HouseListing
    template_name = "HousesApp/forms/submit_house_form.html"
    
    fields = [
        'nome_do_proprietario',
        'sobrenome_do_proprietario',
        'contacto_principal',
        'contacto_secúndario',
        'preço',
        'meses_adiantados',
        'cidade',
        'distrito',
        'bairro',
        'numero_de_divisoes',
        'mobiliada',
        'vedada'
    ]

    permission_denied_message = 'Login is required'

    def form_valid(self,form):
        form.instance.create_by_user = self.request.user
        return super().form_valid(form)
