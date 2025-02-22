# Generated by Django 4.1 on 2022-10-28 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedulee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('link', models.CharField(max_length=256)),
                ('amount', models.BigIntegerField()),
                ('akhir_waktu', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('cloth_model', models.CharField(choices=[('kemeja', 'Kemeja'), ('kaos', 'Kaos'), ('celana', 'Celana'), ('rok', 'Rok'), ('sepatu', 'Sepatu'), ('aksesoris', 'Aksesoris'), ('lainnya', 'Lainnya')], default='kemeja', max_length=30)),
                ('material', models.CharField(choices=[('katun', 'Katun'), ('linen', 'Linen'), ('denim', 'Denim'), ('kulit', 'Kulit'), ('polyester', 'Polyester'), ('suede', 'Suede'), ('sutra', 'Sutra'), ('velvet', 'Velvet'), ('rajut', 'Rajut'), ('rayon', 'Rayon'), ('jersey', 'Jersey'), ('twistcone', 'Twistcone'), ('lainnya', 'Lainnya')], default='katun', max_length=30)),
                ('type', models.CharField(choices=[('perempuan', 'Perempuan'), ('laki', 'Laki-laki'), ('anakPerempuan', 'Anak perempuan'), ('anakLaki', 'Anak laki-laki')], default='perempuan', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
