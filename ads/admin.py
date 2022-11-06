from django.contrib import admin

from ads.models import Ads, Categories
from users.models import Location, User

admin.site.register(Location)
admin.site.register(User)
admin.site.register(Ads)
admin.site.register(Categories)
