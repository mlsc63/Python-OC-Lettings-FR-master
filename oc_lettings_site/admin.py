from django.contrib import admin


from app.models import Address
from profiles.models import Profile
from letting.models import Letting


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
