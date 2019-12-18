from django.contrib import admin
# import your models here
from .models import Demon, Soul, Sin

# Register your models here
admin.site.register(Demon)
admin.site.register(Soul)
admin.site.register(Sin)