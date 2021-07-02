from .models import HouseListing
from .forms import HouseListingForm, HousePictureForm

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

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
    form_class = HouseListingForm
    template_name = "HousesApp/houses_create.html"
    permission_denied_message = 'Login is required'

    def form_valid(self,form):
        form.instance.create_by_user = self.request.user
        return super().form_valid(form)

class HouseUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = HouseListing
    form_class = HouseListingForm
    template_name = "HousesApp/houses_update.html"
    context_object_name = "house"
    permission_denied_message = 'Login is required'

    def test_func(self):
        current_listing_creator = self.get_object().create_by_user
        requesting_user = self.request.user
        return requesting_user == current_listing_creator

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