# Generated by Django 4.0.4 on 2022-05-16 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_feature_details_feature_location_feature_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='location',
        ),
    ]
