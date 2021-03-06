# Generated by Django 2.2.6 on 2019-10-31 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateTimeField(null=True)),
                ('habla_castellano', models.BooleanField(null=True)),
                ('genero', models.BooleanField(null=True)),
                ('fecha_examen', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Prueba',
                'verbose_name_plural': 'Pruebas',
                'ordering': ['-fecha_examen'],
            },
        ),
    ]
