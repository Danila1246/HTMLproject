from django.shortcuts import render, reverse, redirect
from .models import Advertisment
from .forms import AdvertisementForm
# Create your views here.


def index(request):
    advertisements = Advertisment.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)



def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisment(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            return redirect(reverse('main-page'))
    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)