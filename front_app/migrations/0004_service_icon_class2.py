# Generated by Django 3.2.11 on 2022-05-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0003_auto_20220511_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon_class2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
