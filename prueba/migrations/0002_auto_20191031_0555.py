# Generated by Django 2.2.6 on 2019-10-31 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenico', 'Femenino')], max_length=100, null=True),
        ),
    ]