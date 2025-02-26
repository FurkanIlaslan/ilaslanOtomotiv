# Generated by Django 4.2.3 on 2024-03-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Araclar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim1', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı1')),
                ('resim2', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı2')),
                ('resim3', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı3')),
                ('resim4', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı4')),
                ('resim5', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı5')),
                ('resim6', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı6')),
                ('resim7', models.FileField(null=True, upload_to='araclar/', verbose_name='Araç Fotografı7')),
                ('fiyat', models.IntegerField()),
                ('marka', models.CharField(max_length=50)),
                ('seri', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('yıl', models.CharField(max_length=20)),
                ('yakit', models.CharField(max_length=50)),
                ('vites', models.CharField(max_length=50)),
                ('aracDurumu', models.CharField(max_length=50)),
                ('km', models.CharField(max_length=50)),
                ('kasaTipi', models.CharField(max_length=50)),
                ('motorGucu', models.CharField(max_length=50)),
                ('motorHacmi', models.CharField(max_length=50)),
                ('cekisTipi', models.CharField(max_length=50)),
                ('renk', models.CharField(max_length=50)),
            ],
        ),
    ]
