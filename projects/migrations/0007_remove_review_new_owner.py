# Generated by Django 3.1.6 on 2022-02-22 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_review_new_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='new_owner',
        ),
    ]
