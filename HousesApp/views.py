from .models import HouseListing
from .forms import HouseListingForm, HousePictureForm
from .mixins import UserOwnsHouseMixin

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)

# Create your views here.
class HomeView(TemplateView):
    template_name = "HousesApp/houses_home.html"

class HousesListView(ListView):
    model = HouseListing
    context_object_name = "houses"
    template_name = "HousesApp/houses_list.html"

    def get_queryset(self):
        listings = HouseListing.objects.all()
        
        if self.request.GET.__contains__('cidade'):
            cidade = self.request.GET['cidade']
            if cidade != "all":
               listings = listings.filter(cidade__icontains=cidade)

        if self.request.GET.__contains__('distrito'):
            distrito = self.request.GET['distrito']
            
            if distrito != "":
                listings = listings.filter(distrito__icontains=distrito)

        if self.request.GET.__contains__('price_range'):
            price_range = self.request.GET['price_range']

            if price_range != "all":
                if price_range == "low":
                    min_price = 500
                    max_price = 5000

                if price_range == "medium":
                    min_price = 5000
                    max_price = 15000

                if price_range == "high":
                    min_price = 15000
                    max_price = 25000

                listings = listings.filter(preço__range=(min_price,max_price))

        if self.request.GET.__contains__('room_count'):
            room_count = self.request.GET['room_count']
            try:
                room_count = int(room_count)

                if room_count > 0:
                    listings = listings.filter(numero_de_divisoes=room_count)
                
            except Exception as e:
                print("Room count not valid")

        return listings

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.__contains__('cidade'):
            context['cidade'] = self.request.GET['cidade']

        if self.request.GET.__contains__('distrito'):
            context['distrito'] = self.request.GET['distrito']

        if self.request.GET.__contains__('price_range'):
            context['price_range'] = self.request.GET['price_range']

        if self.request.GET.__contains__('room_count'):
            context['room_count'] = self.request.GET['room_count']

        return context

class HouseDetailView(DetailView):
    model = HouseListing
    context_object_name = "house"
    template_name = "HousesApp/houses_details.html"

class HouseCreateView(LoginRequiredMixin,CreateView):
    form_class = HouseListingForm
    template_name = "HousesApp/houses_create.html"
    permission_denied_message = 'Login is required'

    def form_valid(self,form):
        form.instance.create_by_user = self.request.user
        return super().form_valid(form)

class HouseUpdateView(LoginRequiredMixin,UserOwnsHouseMixin,UpdateView):
    model = HouseListing
    form_class = HouseListingForm
    template_name = "HousesApp/houses_update.html"
    context_object_name = "house"
    permission_denied_message = 'Login is required'

class HouseDeleteView(LoginRequiredMixin,UserOwnsHouseMixin,DeleteView):
    model = HouseListing
    template_name = "HousesApp/houses_confirm_delete.html"
    context_object_name = "house"

    def get_success_url(self):
        return reverse('house_user_houses')

class UserHouseListView(LoginRequiredMixin,ListView):
    model = HouseListing
    template_name = "HousesApp/houses_user_houses.html"
    context_object_name = "houses"

    def get_queryset(self):
        return HouseListing.objects.filter(create_by_user=self.request.user)

def upload_listing_picture(request,listing_pk):

    house = get_object_or_404(HouseListing,pk=listing_pk)

    if request.user != house.create_by_user:
        return redirect(house)

    form = HousePictureForm()

    if request.method == 'POST':
        
        form = HousePictureForm(request.POST,request.FILES)

        if form.is_valid():
            form.instance.house = house
            form.save()
            return redirect(house)

    return render(request,'HousesApp/upload_image.html',context={'house' : house, 'form' : form})