from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles_index(request):
    profiles_list = Profile.objects.all()
    print(profiles_list)
    context = {'profiles_list': profiles_list}
    return render(request, 'procfile/index.html', context)


def profile(request, username):
    def_profile = Profile.objects.get(user__username=username)
    context = {'profile': def_profile}
    return render(request, 'procfile/profile.html', context)
