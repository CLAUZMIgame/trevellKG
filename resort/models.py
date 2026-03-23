from django.conf import settings
from django.db import models


class Resort(models.Model):
    REGION_CHOICES = [
        ('issyk_kul_north', 'Северный берег Иссык-Куля'),
        ('issyk_kul_south', 'Южный берег Иссык-Куля'),
        ('bishkek', 'Бишкек'),
        ('chui', 'Чуйская область'),
        ('osh', 'Ошская область'),
    ]

    title = models.CharField(max_length=180)
    region = models.CharField(max_length=40, choices=REGION_CHOICES)
    location = models.CharField(max_length=180)
    description = models.TextField()
    short_description = models.CharField(max_length=220)
    price_from = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image_url = models.URLField(blank=True)
    has_pool = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=True)
    has_parking = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', '-rating', 'price_from']

    def __str__(self):
        return self.title


class BookingRequest(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='requests')
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Заявка: {self.name} -> {self.resort.title}'


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'resort')

    def __str__(self):
        return f'{self.user} -> {self.resort}'
