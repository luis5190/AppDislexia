# Generated by Django 2.1.5 on 2019-10-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0006_auto_20191012_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagen',
            field=models.ImageField(null=True, upload_to='projects'),
        ),
    ]
