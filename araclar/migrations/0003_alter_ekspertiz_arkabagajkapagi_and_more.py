# Generated by Django 4.2.3 on 2024-03-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('araclar', '0002_ekspertiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekspertiz',
            name='arkaBagajKapagi',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='arkaTampon',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='motorHacmi',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='motorKaputu',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='onTampon',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='sagArkaKapi',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='sagMarspiyel',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='sagOnCamurluk',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='sagOnKapi',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='solArkaCamurluk',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='solArkaKapi',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='solMarspiyel',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='solOnCamurluk',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='solOnKapi',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ekspertiz',
            name='tavan',
            field=models.CharField(choices=[('Boyalı', 'Boyalı'), ('Degişen', 'Değişen'), ('Orijinal', 'Orijinal')], max_length=50),
        ),
    ]