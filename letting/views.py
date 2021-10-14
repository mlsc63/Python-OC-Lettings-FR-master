from django.shortcuts import render
from .models import Letting

def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'letting/lettings_index.html', context)


def letting(request, letting_id):
    def_letting = Letting.objects.get(id=letting_id)
    context = {
        'title': def_letting.title,
        'address': def_letting.address,
    }
    return render(request, 'letting/letting.html', context)
