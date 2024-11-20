from django.contrib import admin
from .models import User
 
# register the User so you can access it in the UI on the localhost


admin.site.register(User)