# Generated by Django 3.1.6 on 2022-02-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20220222_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='new_owner',
            field=models.TextField(blank=True, null=True),
        ),
    ]
