from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Languages, Quiz, Information, Room, Message])