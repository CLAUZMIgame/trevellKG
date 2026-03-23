from django.contrib import admin
from .models import BookingRequest, Favorite, Resort


@admin.register(Resort)
class ResortAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'location', 'price_from', 'rating', 'featured')
    list_filter = ('region', 'featured', 'has_pool', 'has_wifi')
    search_fields = ('title', 'location', 'description')


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'resort', 'phone', 'created_at')
    search_fields = ('name', 'phone', 'email')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'resort')
