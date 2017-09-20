from django.shortcuts import render
from .models import Address
from .forms import PostForm

# Create your views here.
def address_list(request):
    addresses=Address.objects.order_by('name')
    return render(request, 'howdy/address_list.html', {'addresses':addresses})

def address_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            address = form.save()
            address.save()
    form = PostForm()    
    return render(request, 'howdy/address_new.html', {'form': form})

def home(request):
    return render(request, 'howdy/index.html', {})