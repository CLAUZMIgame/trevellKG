from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('region', models.CharField(choices=[('issyk_kul_north', 'Северный берег Иссык-Куля'), ('issyk_kul_south', 'Южный берег Иссык-Куля'), ('bishkek', 'Бишкек'), ('chui', 'Чуйская область'), ('osh', 'Ошская область')], max_length=40)),
                ('location', models.CharField(max_length=180)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=220)),
                ('price_from', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('image_url', models.URLField(blank=True)),
                ('has_pool', models.BooleanField(default=False)),
                ('has_wifi', models.BooleanField(default=True)),
                ('has_parking', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-featured', '-rating', 'price_from']},
        ),
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='resort.resort')),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='resort.resort')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
            options={'unique_together': {('user', 'resort')}},
        ),
    ]
