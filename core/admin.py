from django.contrib import admin
from core.models import Restaurant, RestaurantMenus, Review, ReviewDietary

admin.site.register(Restaurant)
admin.site.register(RestaurantMenus)
admin.site.register(Review)
admin.site.register(ReviewDietary)