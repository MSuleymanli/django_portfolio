from django.contrib import admin # type: ignore
from .models import Portfo,Contact
# Register your models here.
admin.site.register(Portfo)
admin.site.register(Contact)