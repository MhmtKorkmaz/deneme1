# Generated by Django 4.1.3 on 2022-11-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constraction',
            name='detay',
            field=models.TextField(blank=True, null=True, verbose_name='Proje Detayları'),
        ),
        migrations.AddField(
            model_name='constraction',
            name='maliyet',
            field=models.IntegerField(blank=True, null=True, verbose_name='Maliyet'),
        ),
        migrations.AddField(
            model_name='constraction',
            name='proje_user',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Proje Sorumlusu'),
        ),
        migrations.AlterField(
            model_name='constraction',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Proje Adı'),
        ),
    ]
