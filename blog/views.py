from django.shortcuts import render
from blog.models import Projek

# Create your views here.
def indeks(request):
    projek1 = Projek.objects.all()
    hal = {
        'projek1':projek1
        }
    return render(request, 'indeks.html', hal)

def detail(request, pk):
    projek2 = Projek.objects.get(pk=pk)
    hal = {
        'projek2':projek2
        }
    return render(request, 'detail.html', hal)

